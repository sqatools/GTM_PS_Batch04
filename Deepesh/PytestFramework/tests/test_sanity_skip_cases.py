import pytest

env = 'BETA'

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
@pytest.mark.skip
def test_subtraction():
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170


@pytest.mark.smoke
def test_fun4():
    num1 = 20
    num2 = 30
    assert num1 + num2 == 50

@pytest.mark.smoke
@pytest.mark.skipif(env == 'PROD', reason="This test is not allowed in production")
def test_fun5():
    num1 = 20
    num2 = 30
    assert num1 * num2 == 500

@pytest.mark.sanity
@pytest.mark.skip
def test_fun6():
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170
