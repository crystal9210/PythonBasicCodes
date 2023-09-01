# use "uvicorn easyFastApi:api --reload" command in an command line and start/launch a server
from fastapi import FastAPI
from typing import Optional,List
from pydantic import BaseModel, Field

class ShopInfo(BaseModel):
  name:str
  location:str

class Item(BaseModel):
  name:str=Field(min_length=1,max_length=25)
  description:Optional[str]=None
  price:int
  tax:Optional[float]=None

class Data(BaseModel):
  shop_info:Optional[ShopInfo]
  items:List[Item]

api=FastAPI() #make an instance

# endpoints of 'get' method

@api.get("/") #instruction of http mapping in this app;"decorator"
async def index():  
  return {"id":1,"message":"Hello World"}

# access url ".../items/{any number is okey}"
@api.get('/items/{item_id}')
def read_item(item_id:int, q:Optional[str]=None):
  return {'item_id':item_id,'q':q}

@api.get('/animals/')
async def animal(animal_name:Optional[str]=None,animal_num:Optional[int]=None):
  return {
    'animal_name':animal_name,
    'animalnum':animal_num
    }
# If you access to '.../animals/cat?animal_num=2' , you get '{"animal_name": "cat","animalnum": 2}' on your browser.


#add:'async' is used to define a function as asynchronous, enabling it to execute asynchronously.

# add:The API endpoint is scanned sequentially from the top of the file, and the first one that meets the conditions is applied.


# endpoints of 'post' method

@api.post('/')
async def index(data:Data):
  return {'data':data}


@api.post('/item/')
async def create_item(item:Item):
  return {"message":f"{item.name}は、{item.description}であり、税込み価格{int(item.price*item.tax)}円です。"}
# access to '/docs' and try it out.




