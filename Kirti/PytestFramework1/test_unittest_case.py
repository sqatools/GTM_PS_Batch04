
def test_addition(fixturesetup):
    Num1 = 10
    Num2 = 20
    print("Addition", Num1+Num2)

def test_substration(fixturesetup):
    Num1 = 20
    Num2 = 30
    print("Substration",Num1-Num2)

#python -m pytest -v -s .\test_unittest_case.py