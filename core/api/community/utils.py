# config.py or settings.py
import cloudinary
import cloudinary.uploader
import os
from decouple import config


# Configure Cloudinary
cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
    secure=True
)


# services/cloudinary_service.py
import cloudinary.uploader
from fastapi import HTTPException, UploadFile
from typing import Dict, Optional
import uuid

class CloudinaryService:
    @staticmethod
    async def upload_image(
        file: UploadFile,
        folder: str = "posts",
        public_id: Optional[str] = None
    ) -> Dict:
        """
        Upload image to Cloudinary
        """
        try:
            # Validate file type
            if not file.content_type.startswith('image/'):
                raise HTTPException(
                    status_code=400, 
                    detail="Only image files are allowed"
                )
            
            # Generate unique public_id if not provided
            if not public_id:
                public_id = f"{folder}_{uuid.uuid4().hex}"
            
            # Read file content
            file_content = await file.read()
            
            # Upload to Cloudinary
            result = cloudinary.uploader.upload(
                file_content,
                public_id=public_id,
                folder=folder,
                resource_type="image",
                overwrite=True,
                transformation=[
                    {"quality": "auto", "fetch_format": "auto"},
                    {"width": 1000, "height": 1000, "crop": "limit"}
                ]
            )
            
            return {
                "public_id": result["public_id"],
                "url": result["secure_url"],
                "width": result["width"],
                "height": result["height"],
                "format": result["format"],
                "bytes": result["bytes"]
            }
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to upload image: {str(e)}"
            )
    
    @staticmethod
    def delete_image(public_id: str) -> bool:
        """
        Delete image from Cloudinary
        """
        try:
            result = cloudinary.uploader.destroy(public_id)
            return result.get("result") == "ok"
        except Exception as e:
            print(f"Failed to delete image: {str(e)}")
            return False