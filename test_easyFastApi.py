# before execute this file , you should execute easyFastApi.py and check the url of the uvicorn server by access to '/docs' and execute api test , and so get the url and input the url to the variable 'url below' 
import requests
import json

def main():
  url='http://127.0.0.1:8000/item/'
  body={
  "name": "Kii tyan",
  "description": "neko",
  "price": 100,
  "tax": 1.1
  }
  res=requests.post(url,json.dumps(body))
  print(res.json())

if __name__=='__main__':
  main()