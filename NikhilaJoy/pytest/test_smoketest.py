import pytest
env='PROD'
@pytest.mark.add
@pytest.mark.skipif(env== 'PROD' ,reason ="this is not allowed")
def test_addition():
    num1=20
    num2=100
    assert num1 + num2 == 120
def test_multi():
    num1=20
    num2=100
    assert num1 * num2 == 12

@pytest.mark.add
def test_sub():
    num1=100
    num2=20
    assert num1 - num2 == 80




