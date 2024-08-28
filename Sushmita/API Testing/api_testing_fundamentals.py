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


"""
URI = "https://api.restful-api.dev/objects"
# https :  protocol
# api.restful-api.dev : server address
# /objects : API End point.

response = requests.request("GET", URI)
print(response.json(), response.status_code)
"""

def api_get_response():

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())

api_get_response()
