from pydantic import BaseModel,Field,field_validator
from typing import Optional,List
from .exceptions import PostCreateValidationsException


class PostCreateSchema(BaseModel):
    post_owner:str=Field(...)
    title:str=Field(...)
    content:str=Field(...)

    @field_validator("post_owner",mode="after")
    def owner(cls,value):
        if len(value) == 0:
            raise PostCreateValidationsException(
                status_code=401,
                detail="Validation error",
                solution="post_owner field required!!!"
            )
        return value
    @field_validator("title",mode="after")
    def title(cls,value):
        if len(value) == 0:
            raise PostCreateValidationsException(
                status_code=401,
                detail="Validation error",
                solution="title field required!!!"
            )
        return value

    @field_validator("content",mode="after")
    def content(cls,value):
        if len(value) == 0:
            raise PostCreateValidationsException(
                status_code=401,
                detail="Validation error",
                solution="content field required!!!"
            )
        return value
    


class PostCreateResponse(BaseModel):
    status:Optional[bool] = True
    message:str
    
class GetAllPostsResponseModel(BaseModel):
    status:Optional[bool] = True
    message:str
    posts:List