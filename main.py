# use "uvicorn main:api --reload" command in an command line and start/launch a server
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

api=FastAPI() #make an instance

@api.get("/") #instruction of http mapping in this app;"decorator"
async def index():  
  return {"id":1,"message":"Hello World"}

# access url ".../items/{any number is okey}"
@api.get('/items/{item_id}')
def read_item(item_id:int, q:str=None):
  return {'item_id':item_id,'q':q}


#add:'async' is used to define a function as asynchronous, enabling it to execute asynchronously.


