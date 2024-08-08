import pytest
from data_file import *
@pytest.mark.parametrize("username, password", parm_data)
def test_login(username, password):
    print("credentials :", username, password)


