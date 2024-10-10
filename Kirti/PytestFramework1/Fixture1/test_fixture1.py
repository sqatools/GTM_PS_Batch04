
import pytest

@pytest.fixture(scope='function')
def fixturesetup():
    print("\n----- test cases execution started----\n")
    yield  # teardown
    print("--- test case execution completed ----")

def test_addition(fixturesetup):
    Num1 = 10
    Num2 = 20
    print("Addition", Num1+Num2)

def test_substration(fixturesetup):
    Num1 = 20
    Num2 = 30
    print("Substration",Num1-Num2)
