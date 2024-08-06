import pytest

@pytest.mark.smoke
def test_addition():
    num1=10
    num2=20
    assert num1+num2==30

@pytest.mark.sanity
def test_multication():
    num1=20
    num2=10
    assert num1 * num2 ==300

@pytest.mark.smoke
def test_substraction():
    num1=50
    num2=10
    assert num1 - num2==40

