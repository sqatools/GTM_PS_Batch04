import pytest

env = 'BETA'

@pytest.mark.order(2)
@pytest.mark.smoke
def test_addition():
    num1 = 20
    num2 = 30
    assert num1 + num2 == 50

@pytest.mark.order(6)
@pytest.mark.smoke
def test_dmultiplication():
    num1 = 20
    num2 = 30
    assert num1 * num2 == 500

@pytest.mark.order(3)
@pytest.mark.sanity
@pytest.mark.skip
def test_btraction():
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170


@pytest.mark.order(4)
@pytest.mark.smoke
def test_bb_cfun4():
    num1 = 20
    num2 = 30
    assert num1 + num2 == 50

@pytest.mark.order(5)
def test_efun5():
    num1 = 20
    num2 = 30
    assert num1 * num2 == 500

@pytest.mark.order(1)
def test_aa_ffun6():
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170
