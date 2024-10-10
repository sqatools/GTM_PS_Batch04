def test_addition():
    num1 = 10
    num2 = 20
    assert num1 + num2 == 30

def test_multiplication():
    num1 = 10
    num2 = 20
    assert num1 * num2 == 30

def test_substration():
    num1 = 20
    num2 = 10
    assert num1 - num2 == 10

#python -m pytest -v .\test_smoke_cases.py