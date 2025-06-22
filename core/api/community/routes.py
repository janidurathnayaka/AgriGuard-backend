from fastapi import APIRouter,status,File,UploadFile,Form
from database.db import db_dependencie 
from .schemas import PostCreateSchema,PostCreateResponse,GetAllPostsResponseModel
from .service import CreateNewPostService,GetAllPostsService


router = APIRouter()



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
@router.get("/",status_code=status.HTTP_200_OK,description="Get all posts",response_model=GetAllPostsResponseModel)
def getAllPosts(db:db_dependencie):
    res = GetAllPostsService(db)
    return GetAllPostsResponseModel(
        message="Posts retrived succuss!",
        posts=res
    )
    