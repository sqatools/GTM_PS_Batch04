import pytest


@pytest.mark.t1
@pytest.mark.smoke
def test_addition():
    num1 = 10
    num2 = 20
    assert num1 + num2 == 30


@pytest.mark.smoke
def test_multiplication():
    num1 = 20
    num2 = 30
    assert num1 * num2 == 900


@pytest.mark.sanity
def test_subtraction():
    num1 = 100

    num2 = 50
    assert num1 - num2 == 50


@pytest.mark.t1
@pytest.mark.sanity
def test_fun4():
    num1 = 20
    num2 = 30
    assert num1 + num2 == 50


@pytest.mark.smoke
def test_fun5():
    num1 = 20
    num2 = 30
    assert num1 * num2 == 500


@pytest.mark.sanity
def test_fun6():
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170
