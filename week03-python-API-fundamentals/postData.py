import requests
import json

from aiohttp import payload

#get_url="https://api.restful-api.dev/objects/7"
#response=requests.get(get_url)
#data=response.json()
#print(data)


post_url="https://api.restful-api.dev/objects"

#payload(content to be post)
payload_json={
  "name": "Apple MacBook Pro 55",
  "data": {
    "year": 2051,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "2 TB"
  }
}
json_data=json.dumps(payload_json)
#header(to define data structure .,json , text , xml )

header_post={
    "Content-Type": "application/json"
    }
post_response = requests.post(post_url,headers=header_post,json=payload_json)

if post_response.status_code== 200 or post_response.status_code == 201:
    print(f"Post Request Successful:{post_response.status_code}")
    print(f"Response: {post_response.json()}")
else:
        print(f"Post request failed :{post_response.status_code}")
        print(f"Response: {post_response.text}")

get_url="https://api.restful-api.dev/objects"
response=requests.get(get_url)
data=response.json()
print(data)
