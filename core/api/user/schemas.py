from pydantic import BaseModel,Field,field_validator
from .exceptions import NotValidEmailException
from fastapi import status
from typing import Optional

class RegisterRequestSchema(BaseModel):
    email:str = Field(...)
    id:str = Field(...)

    @field_validator("email",mode="after")
    def isEmail(cls,value:str):
        if not value.endswith(".com"):
            raise NotValidEmailException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email error",solution="Enter valid email address")
        return value
    
    @field_validator("id",mode="before")
    def FieldRequired(cls,value:str):
        if not value or len(value)==0:
            raise NotValidEmailException(status_code=status.HTTP_400_BAD_REQUEST,detail="Userid error",solution="User id field required")
        return value
    

class RegisterUserResponse(BaseModel):
    status:Optional[bool] = True
    message:str
    


    