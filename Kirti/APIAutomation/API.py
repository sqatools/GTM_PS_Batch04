import requests
#
# URI = "https://api.restful-api.dev/objects"
# # https :  protocol
# # api.restful-api.dev : server address
# # /objects : API End point.
#
# response = requests.request("GET", URI)
# print(response.json(), response.status_code)

# import requests
#
# URI = "https://api.restful-api.dev/objects"
#
# XYZ = requests.request("GET",URI)
# print(XYZ)
#
# print(XYZ.json(),XYZ.status_code)

"**********************************************"

# import requests
#
# def AssetAPIResponse():
#
#     URL = "https://api.restful-api.dev/objects"
#
#     Payload = {}
#     headers = {}
#
#     response = requests.request("GET",URL, headers=headers, data=Payload)
#
#     data = response.json()
#     print(data)
#
#     expected_value = "Google Pixel 6 Pro" #"Samsung"
#
#
#     output = False
#     for info in data:
#         if info['name'] == expected_value:
#             output = True
#             break
#         else:
#             continue
#
#     assert output, f"{expected_value} Expected value is not present"
# AssetAPIResponse()


#GET Specific Data

def get_specific_data_GET():

    URL = "https://api.restful-api.dev/objects?id=3&id=5&id=10"
    Payload = {}
    Headers = {}

    response = requests.request(PUT,)
