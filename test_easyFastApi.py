# Before executing this file, execute 'easyFastApi.py' and start the UVicorn server. Then, access the '/docs' endpoint from a browser, perform a test with the 'POST' method, check the URL, and store that URL in the 'url' variable below. 
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