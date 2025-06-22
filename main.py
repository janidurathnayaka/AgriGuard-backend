from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from core.api.user.routes import router as UserRouter
from core.api.community.routes import router as CommunityRouter


app = FastAPI(title="AgriGuard Api",version="1.0")

app.include_router(prefix="/user",router=UserRouter,tags=["User"])
app.include_router(prefix="/community",router=CommunityRouter,tags=["Community"])



@app.exception_handler(HTTPException)
async def exception_handler(request,exe:HTTPException):
    return JSONResponse(status_code=exe.status_code,content={
        "error":exe.detail,
        "solution":exe.solution
    })

