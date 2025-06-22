from .exceptions import OwnerNotFoundException
from fastapi import status

def CreatePostRepository(post,db):
    """Create new record in database"""
    #Check is owner is exiss user in users table
    user = db.table("users").select("*").eq("id",post["post_owner"]).execute()
    if len(user.data) == 0:
        raise OwnerNotFoundException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid user id: {post["post_owner"]}",
            solution="Please checkk admin id again"
            )
    post_data = db.table("posts").insert(post).execute()
    if len(post_data.data) > 0:
        return post_data.data[0]["id"]
    return None
        