"""
What is API (Application Programming Interface)

There are three layers in any software
1. Presentation layer
2. Application Layer
3. Database Layer
API works under application layer to receive request and send response to the client

API works on HTTP protocol
There are some methods available in HTTP

1. GET
2. POST
3. PUT
4. PATCH
5. DELETE

Each method has there response code, here is the range of response
101 - 199 : Informational Response
200 - 299 : Success Response
300 - 399 : Re-directional Response
400 - 499 : Client Error
500 - 599 : Server Error

https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#information_responses

"""

import requests
import json
"""
pip install requests
"""

"""
URI = "https://api.restful-api.dev/objects"
# https :  protocol
# api.restful-api.dev : server address
# /objects : API End point.

response = requests.request("GET", URI)
print(response.json(), response.status_code)
"""

def get_api_response():

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    expected_value = "Apple MacBook Pro 168"

    print(data)
    output = False
    for info in data:
        if info['name'] == expected_value:
            output = True
            break
        else:
            continue
        #print(info['name'])

    assert output, "required value is not available"


#get_api_response()


def get_specific_ids_info():

    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


get_specific_ids_info()


def get_specific_one_id_info(id):

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


#get_specific_one_id_info("ff80818191937f840191949f9e1a0272")


def create_new_entry_with_post():

    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
      "name": "Apple MacBook Pro 21",
      "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


#create_new_entry_with_post()

# {"id":"ff80818191937f84019194aedada0285","name":"Apple MacBook Pro 21","createdAt":"2024-08-27T16:32:52.958+00:00","data":{"year":2019,"price":1849.99,"CPU model":"Intel Core i9","Hard disk size":"1 TB"}}


def update_entry_with_put(object_id):

    url = f"https://api.restful-api.dev/objects/{object_id}"

    payload = json.dumps({
      "name": "Apple MacBook Pro 102",
      "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "5 TB"
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

# update_entry_with_put("102")
"""
The PUT HTTP method is used to update or replace an 
existing resource on a server with new data or a similar 
resource that has different values. It's often used in RESTful APIs. 

"""


def update_entry_with_patch(object_id):

    url = f"https://api.restful-api.dev/objects/{object_id}"

    payload = json.dumps({"data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB"
      }})
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.text)

#update_entry_with_patch("ff80818191937f84019194aedada0285")


def delete_entry(object_id):

    url = f"https://api.restful-api.dev/objects/{object_id}"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)

#delete_entry("ff80818191937f84019194aedada0285")
