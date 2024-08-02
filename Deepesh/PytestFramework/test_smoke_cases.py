import pytest

@pytest.mark.smoke
def test_addition():
    num1 = 20
    num2 = 30
    assert num1 + num2 == 50

@pytest.mark.smoke
def test_multiplication():
    num1 = 20
    num2 = 30
    assert num1 * num2 == 500

@pytest.mark.sanity
def test_subtraction():
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170
