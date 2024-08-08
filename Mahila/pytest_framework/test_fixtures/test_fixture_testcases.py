import pytest


@pytest.fixture(scope='function')
def setup():
    print("\n--------execution started ----------------\n")
    yield
    print("\n----------execution ended----------\n")

@pytest.fixture(scope='module',autouse=True)
def setup_module():
    print("\n----module level execution started-----\n")
    yield
    print("\n---------module level ended-----\n")

@pytest.fixture(scope='package',autouse=True)
def setup_package():
    print("\n----package level execution started-----\n")
    yield
    print("\n-----package level ended-----\n")

@pytest.fixture(scope='session',autouse=True)
def setup_session():
    print("\n----session level execution started-----\n")
    yield
    print("\n---------session level ended-----\n")



def test_addition(setup):
    a=10
    b=100
    print("addition result :",a+b)
    assert a+b ==110

def test_sub(setup):
    a=100
    b=10
    print("subtraction result :", a - b)
    assert a-b == 1000

