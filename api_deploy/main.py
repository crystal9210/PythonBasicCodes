from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
  x=float
  y=float

app=FastAPI()


@app.get('/')
def index():
  return {'message':'Hello Deta!'}

@app.post('/')
def calc(deta:Data):
  z=deta.x*deta.y
  return {'result':z}
