from base.api_base import APIBase
from resource.api_data.public_api_data import *
import logging

class PublicAPIOperation(APIBase):
    def __init__(self, server):
        super().__init__(server)
        self.server = server
        self.log = logging.getLogger(__name__)

    def get_list_of_all_objects(self):
        self.log.info("get_list_of_all_objects execution started")
        url = f"{protocol}://{self.server}/objects"
        response = self.get_method(url=url)
        return response

    def get_specific_objects_data(self, *args):
        self.log.info("get_specific_objects_data execution started")
        url = f"{protocol}://{self.server}/objects?"
        for id in args:
            url = url+f"id={id}&"

        response = self.get_method(url=url)
        return response
