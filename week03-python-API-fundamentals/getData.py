import json

import requests
get_url="https://api.restful-api.dev/objects"
response=requests.get(get_url)

if response.status_code==200:
    response_dic=response.json()
    print(f"{response_dic}")
    with open("response_file.txt","w") as file:
       json.dump("response_dic",file)
else:
    print(f"Request not successful |"
          f"status_code: {response.status_code} {response.}")