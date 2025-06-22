from fastapi import HTTPException

class PostCreateException(HTTPException):
    pass

class PostCreateValidationsException(PostCreateException):
    """For pydantic valdation error"""
    def __init__(self, status_code, detail:str = None, solution:str=None):
        super().__init__(status_code, detail)
        self.solution = solution


class OwnerNotFoundException(PostCreateException):
    def __init__(self, status_code, detail:str = None, solution:str = None):
        super().__init__(status_code, detail)
        self.solution = solution