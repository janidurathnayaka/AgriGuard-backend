from fastapi import HTTPException

class UserExceptions(HTTPException):
    """Base class for user exceptions"""
    pass

class RegisterException(UserExceptions):
    def __init__(self, status_code:int=500, detail:str=""):
        super().__init__(status_code, detail)
        self.solution = "Try again later"

class NotValidEmailException(UserExceptions):
    def __init__(self, status_code:int=500, detail:str="",solution:str=""):
        super().__init__(status_code, detail)
        self.solution = solution


