from fastapi import APIRouter,status,File,UploadFile,Form
from database.db import db_dependencie 
from .schemas import PostCreateSchema,PostCreateResponse,GetAllPostsResponseModel,UpdatePostSchema
from .service import CreateNewPostService,GetAllPostsService,DeletePostService,UpdatePostService


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
    

@router.delete("/{post_id}",status_code=status.HTTP_200_OK)
def deletePost(post_id:str,db:db_dependencie):
    res = DeletePostService(post_id,db)
    if res is None:
        return {"message":"Post not found"}
    return {"message":"Post deleted succussfully!"}


@router.put("/{post_id}",status_code=status.HTTP_200_OK)
def updatePost(post_id:str,db:db_dependencie,updated_post:UpdatePostSchema):

    res  = UpdatePostService(post_id,db,updated_post.model_dump())
    if res is None:
        return {"message":"Post not found"}
    return {"message":"Post updated succussfully!"}