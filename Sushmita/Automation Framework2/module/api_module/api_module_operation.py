from base.api_base import APIBase
from resource.api_data.public_api_data import *
import logging
import json


class PublicAPIOperation(APIBase):
    def __init__(self, server):
        super().__init__(server)
        self.server = server
        self.log = logging.getLogger(__name__)

    def get_all_objects(self):
        self.log.info("get_list_of_all_objects execution started")
        url = f"{protocol}://{self.server}/objects"
        response, st_code = self.get_method(url=url)
        return response, st_code

    def get_specific_objects_data(self, *args):
        self.log.info("get_specific_objects_data execution started")
        url = f"{protocol}://{self.server}/objects?"
        for id in args:
            url = url + f"id={id}&"

        response, st_code = self.get_method(url=url)
        return response, st_code

    def get_one_specific_object_data(self, object_id):
        self.log.info("get_specific_objects_data execution started")
        url = f"{protocol}://{self.server}/objects/{object_id}"
        response, st_code = self.get_method(url=url)
        return response, st_code

    def create_add_object_via_api(self):
        self.log.info("create_add_object_via_api execution started")
        url = f"{protocol}://{self.server}/objects"
        data_payload = json.dumps(create_object_payload)
        response, st_code = self.post_method(url=url, headers=json_headers, payload=data_payload)
        return response, st_code

    def update_object_data_via_api(self, object_id):
        self.log.info("update_object_data_via_api execution started")
        url = f"{protocol}://{self.server}/objects/{object_id}"
        data_payload = json.dumps(update_data_info_for_object_id)
        response, st_code = self.put_method(url=url, headers=json_headers, payload=data_payload)
        return response, st_code

    def patch_specific_info_object_data_via_api(self, object_id):
        self.log.info("patch_specific_info_object_data_via_api execution started")
        url = f"{protocol}://{self.server}/objects/{object_id}"
        data_payload = json.dumps(update_specific_data_for_object)
        response, st_code = self.patch_method(url=url, headers=json_headers, payload=data_payload)
        return response, st_code

    def delete_specific_object_entry(self, object_id):
        self.log.info("delete_specific_object_entry execution started")
        url = f"{protocol}://{self.server}/objects/{object_id}"
        response, st_code = self.delete_method(url=url)
        return response, st_code
