
import pytest


@pytest.mark.smoke
def test_addition():
    num1 =10
    num2 =20
    assert num1+num2 == 30

@pytest.mark.sanity
def test_multiplication():
    num1 = 10
    num2 = 30
    assert num1*num2 ==400

@pytest.mark.smoke
def test_subtraction():
    num1 = 200
    num2 = 100
    assert num1-num2 ==100


