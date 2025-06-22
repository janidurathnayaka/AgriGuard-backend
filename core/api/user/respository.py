from .exceptions import RegisterException

#Create user in db

def create(user_data,db):
    try:
        ressponse = db.table("users").insert(user_data).execute()
        if ressponse.data:
            print(ressponse.data[0]["id"])
            return ressponse.data[0]["id"]
        
        return None
    except Exception as e:
        raise RegisterException(status_code=400,detail="Register error")