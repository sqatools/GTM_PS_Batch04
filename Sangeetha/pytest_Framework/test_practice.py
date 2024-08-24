import pytest
def test_multipication():
    a=3
    b=4
    assert a * b == 12
def test_m2():
    name="sangeetha"
    assert name.upper()=="SANGEETHA"
@pytest.mark.smoke
def test_login():
    assert "admin"=="admin"



