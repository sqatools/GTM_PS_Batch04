#python -m pytest -v .\test_smoke_cases.py

def test_addition():
    num1=20
    num2=20
    assert num1+num2 == 40

def test_mul():
    num1 = 20
    num2 = 20
    assert num1 * num2 == 40