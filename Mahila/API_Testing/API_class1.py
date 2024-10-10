import requests
URI = "https://api.restful-api.dev/objects"
response = requests.request("GET", URI)
print(response , response.status_code)