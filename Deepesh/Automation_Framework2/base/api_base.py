import requests
import logging


class APIBase:
    def __init__(self, server, protocol="https"):
        self.server = server
        self.protocol = protocol
        self.log = logging.getLogger(__name__)

    def get_method(self, api_end_point=None, url=None, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        if url is not None:
            url = url
        else:
            url = f"{self.protocol}//:{self.server}/{api_end_point}"

        response = requests.request("GET", url, headers=headers, data=payload)
        self.log.info(f"request headers: {headers}")
        self.log.info(f"request payload: {payload}")
        self.log.info(f"{response.json()}")
        self.log.info(f"status code: {response.status_code}")
        self.log.info(f"response header: {response.headers}")
        return response.json(), response.status_code

    def post_method(self, api_end_point=None, url=None, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        if url is not None:
            url = url
        else:
            url = f"{self.protocol}//:{self.server}/{api_end_point}"

        response = requests.request("POST", url, headers=headers, data=payload)
        self.log.info(f"request headers: {headers}")
        self.log.info(f"request payload: {payload}")
        self.log.info(f"{response.json()}")
        self.log.info(f"status code: {response.status_code}")
        self.log.info(f"response header: {response.headers}")
        return response.json(), response.status_code

    def put_method(self, api_end_point=None, url=None, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        if url is not None:
            url = url
        else:
            url = f"{self.protocol}//:{self.server}/{api_end_point}"

        response = requests.request("PUT", url, headers=headers, data=payload)
        self.log.info(f"request headers: {headers}")
        self.log.info(f"request payload: {payload}")
        self.log.info(f"{response.json()}")
        self.log.info(f"status code: {response.status_code}")
        self.log.info(f"response header: {response.headers}")
        return response.json(), response.status_code

    def patch_method(self, api_end_point=None, url=None, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        if url is not None:
            url = url
        else:
            url = f"{self.protocol}//:{self.server}/{api_end_point}"

        response = requests.request("PATCH", url, headers=headers, data=payload)
        self.log.info(f"request headers: {headers}")
        self.log.info(f"request payload: {payload}")
        self.log.info(f"{response.json()}")
        self.log.info(f"status code: {response.status_code}")
        self.log.info(f"response header: {response.headers}")
        return response.json(), response.status_code

    def delete_method(self, api_end_point=None, url=None, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        if url is not None:
            url = url
        else:
            url = f"{self.protocol}//:{self.server}/{api_end_point}"

        response = requests.request("delete", url, headers=headers, data=payload)
        self.log.info(f"request headers: {headers}")
        self.log.info(f"request payload: {payload}")
        self.log.info(f"{response.json()}")
        self.log.info(f"status code: {response.status_code}")
        self.log.info(f"response header: {response.headers}")
        return response.json(), response.status_code
