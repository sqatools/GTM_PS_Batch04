import pytest
from modules.api_module.public_api_operation import PublicAPIOperation
from resource.api_data.public_api_data import *


class TestPublicAPI:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self):
        self.pub_api = PublicAPIOperation(server)

    def test_verify_total_number_of_objects(self):
        response = self.pub_api.get_list_of_all_objects()
        assert len(response) == 13

    def test_verify_specific_objects_data(self):
        response = self.pub_api.get_specific_objects_data(3, 5, 7)
        assert len(response) == 3
