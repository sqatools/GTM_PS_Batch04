import requests

# URI = "https://api.restful-api.dev/objects"
# # https :  protocol
# # api.restful-api.dev : server address
# # /objects : API End point.
#
# response = requests.request("GET", URI)
# print(response.json(), response.status_code)

def get_api_response():

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response


    print(data)

        #print(info['name'])

    # assert output, "required value is not available"
get_api_response()
