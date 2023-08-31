import requests
url='https://jsonplaceholder.typicode.com/posts'

res = requests.get(url)
print(res.status_code)  
# →output:200;this number means 'success'

# extract the content data from the response
print(res.json()[1])
# →If you don't get only [0] property, a substantial amout of information is outputted in JSON format.

# extract specific data from a JSON-formatted single data
print(res.json()[1]['userId'])

print("")

# Making an API request to retrieve data that meets specific criteria,including certain parameters
params={
  'userId':2
}
res2=requests.get(url,params)
print(res2.json())

print("")

print(res2.json()[6])


