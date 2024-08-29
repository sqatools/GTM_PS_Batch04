import pytest
from modules.api_module.public_api_operation import PublicAPIOperation
from resource.api_data.public_api_data import *


class TestPublicAPI:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self):
        self.pub_api = PublicAPIOperation(server)

    def test_verify_total_number_of_objects(self):
        response, st_code = self.pub_api.get_list_of_all_objects()
        assert len(response) == 13
        assert st_code == 200

    def test_verify_specific_objects_data(self):
        response, st_code = self.pub_api.get_specific_objects_data(3, 5, 7)
        assert len(response) == 3
        assert st_code == 200

    def test_verify_for_one_specific_object_id(self):
        response, st_code = self.pub_api.get_specific_objects_data(8)
        assert st_code == 200
        assert len(response) == 1 and response[0]['name'] == 'Apple Watch Series 8'

    def test_verify_for_invalid_object_id(self):
        response, st_code = self.pub_api.get_one_specific_object_data(150)
        assert st_code == 404
        assert "id=150 was not found" in response['error']

    def test_create_an_object_and_verify(self):
        response, st_code = self.pub_api.create_add_object_via_api()
        assert st_code == 200
        assert response['name'] == 'Apple MacBook Pro 120'

    def test_update_an_object_details_and_verify(self):
        create_response, create_st_code = self.pub_api.create_add_object_via_api()
        assert create_st_code == 200
        object_id = create_response["id"]

        response, st_code = self.pub_api.update_object_data_via_api(object_id)
        assert st_code == 200
        assert response['name'] == 'Apple MacBook Pro 150'

    def test_patch_object_detail_and_verify(self):
        create_response, create_st_code = self.pub_api.create_add_object_via_api()
        assert create_st_code == 200
        object_id = create_response["id"]
        response, st_code = self.pub_api.patch_specific_info_object_data_via_api(object_id)
        assert st_code == 200
        assert response['data']['Hard disk size'] == '5 TB'

    def test_delete_object_detail_and_verify(self):
        create_response, create_st_code = self.pub_api.create_add_object_via_api()
        assert create_st_code == 200
        object_id = create_response["id"]
        response, st_code = self.pub_api.delete_specific_object_entry(object_id)
        assert st_code == 200
        assert "has been deleted" in response['message']
