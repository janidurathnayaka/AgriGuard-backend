from fastapi import APIRouter,status
from database.db import db_dependencie
from .schemas import RegisterRequestSchema,RegisterUserResponse
from .service import UserRegisterService

router = APIRouter()


@router.get("/")
def root():
    return "Hello"


#User Register
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=RegisterUserResponse)
def RegisterUser(register_data:RegisterRequestSchema,db:db_dependencie):
    response = UserRegisterService(register_data.model_dump(),db=db)
    print(response)
    if response:
        return RegisterUserResponse(message="User registration succuss")
    else:
        return RegisterUserResponse(status=False,message="User registration failed")

    