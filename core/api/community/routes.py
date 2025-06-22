from fastapi import APIRouter,status,File,UploadFile,Form
from database.db import db_dependencie 
from .schemas import PostCreateSchema,PostCreateResponse
from .service import CreateNewPostService


router = APIRouter()

@router.get("/")
def root():
    return "Hello"

#Create new post
@router.post("/create-post",status_code=status.HTTP_201_CREATED,description="Create new post",response_model=PostCreateResponse)
async def postCreate(
    db:db_dependencie,
    post_owner: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    file: UploadFile = File(None),
    ):


    post = {"post_owner":post_owner,"title":title,"content":content}
    res = await CreateNewPostService(post,db=db,file=file)
    return PostCreateResponse(
        message="Post created succuss!!"
    )


#Get all posts
# @router.get("/",status_code=status.HTTP_200_OK,description="Get all posts")
    