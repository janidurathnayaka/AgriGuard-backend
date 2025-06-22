from .respository import CreatePostRepository,GetAllPostRepository
from .utils import CloudinaryService
import uuid

#Create new post service

async def CreateNewPostService(post,db,file):


    upload_result =  await CloudinaryService.upload_image(
            file=file,
            folder="posts",
            public_id=f"post_{post['post_owner']}_{uuid.uuid4().hex}"
        )
    post["img"] = upload_result["url"]
    return CreatePostRepository(post,db)


#Get all posts
def GetAllPostsService(db):
    response = GetAllPostRepository(db)
    if response is None:
        return None
    return response