
from typing import Optional,List
from fastapi import FastAPI, HTTPException, Response,status
from fastapi.params import Body, Depends
import psycopg2
from pydantic import BaseModel
from random import randrange
import time
from sqlalchemy import select
from . import models,schemas,utils
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from .routers import post,user,auth,vote
from fastapi.middleware.cors import CORSMiddleware


my_posts =[{"title":"title of post 1","content":"content of post 1","id":1}
           ,{"title":"title of post 2","content":"content of post 2",id:2}]

# models.Base.metadata.create_all(bind = engine)
app = FastAPI()
###    return {"message":"Hello World"}

origins = ["https://www.google.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {"message" : "Hello World1234"}

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)