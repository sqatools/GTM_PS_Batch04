import pytest

def mul():
    num1 = 5
    num2 = 4
    assert num1*num2==20

def sub():
    num1 = 5
    num2 = 4
    assert num1 - num2 ==20

@pytest.mark.skip
def add():
    num1=2
    num2=10
    assert num1+num2==12