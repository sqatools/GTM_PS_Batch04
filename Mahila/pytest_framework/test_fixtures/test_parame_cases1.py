import pytest
from data_file import *

@pytest.mark.parametrize("username, password", parm_data)
def test_login(username, password):
    print("credentials :", username, password)


@pytest.mark.parametrize("username,password",excel_data)
def test_login_1(username,password):
    print("credentials : ", username,password)

@pytest.mark.parametrize("username,password",bulk_data)
def test_login_2(username,password):
    print("credentials :" , username,password)
