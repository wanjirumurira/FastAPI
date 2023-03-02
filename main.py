from urllib import response
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional
from random import randrange

my_posts =[{"title": "title of post 1", "content":"content of post 1", "id" :1}]

app = FastAPI()
#used to create the schema of our APIS
class Post(BaseModel):
    title: str
    content : str
    published : bool = True
    rating: Optional[int] = None

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def get_posts():
    return {"data" : my_posts}

@app.post("/")
def get_posts():
    return {"data" : my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000000)
    my_posts.append(post_dict)
    return{"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(int(id))
    if not post:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, 
                             detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail" : f"post with id: {id} was not found"}
    return {"post_detail": post}

