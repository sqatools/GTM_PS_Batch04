def test_addition(first_setup1):
    num1 = 20
    num2 = 30
    print("addition output :", num1+num2)
    assert num1 + num2 == 50


def test_multiplication(first_setup1):
    num1 = 20
    num2 = 30
    print("multiply output :", num1*num2)
    assert num1 * num2 == 500


def test_subtraction(first_setup1):
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170
