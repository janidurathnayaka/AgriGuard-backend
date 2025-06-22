from .respository import create


#UserRegisterService
def UserRegisterService(user_data,db):
    return create(user_data,db)