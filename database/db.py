from decouple import config
from fastapi import Depends
from supabase import Client,create_client
from typing import Annotated


DATABASE_URL = config("DATABASE_URL")
DATABASE_KEY=config("DATABASE_KEY")


superbase:Client = create_client(DATABASE_URL,DATABASE_KEY)

def get_db():
    return superbase


db_dependencie = Annotated[Client,Depends(get_db)]



