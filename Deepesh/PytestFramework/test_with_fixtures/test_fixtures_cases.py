import pytest
"""
# fixture : fixture is setup and teardown for test case execution which has different scope
function: function level scope executes for each test function.
module : module level scope executes for each module file.
package : package level scope executes for each package which may contains multiple modules.
session : session level scope execute once for each session.
class : class level scope executes for each class.
"""

@pytest.fixture(scope='function')
def setup():
    print("\n----- test cases execution started----\n")
    yield  # teardown
    print("--- test case execution completed ----")


@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print("\n--- Module execution started ----")
    yield
    print("\n--- Module execution completed ----")

@pytest.fixture(scope='package', autouse=True)
def setup_package():
    print("\n--- Package execution started ----")
    yield
    print("\n--- Package execution completed ----")

@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print("\n--- Session execution started ----")
    yield
    print("\n--- Session execution completed ----")


def test_addition(setup):
    num1 = 20
    num2 = 30
    print("addition output :", num1+num2)
    assert num1 + num2 == 50


def test_multiplication(setup):
    num1 = 20
    num2 = 30
    print("multiply output :", num1*num2)
    assert num1 * num2 == 500



def test_subtraction(setup):
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170



def test_fun4(setup):
    num1 = 20
    num2 = 30
    print("addition :", num1+num2)
    assert num1 + num2 == 50


def test_fun5(setup):
    num1 = 20
    num2 = 30
    assert num1 * num2 == 500


def test_fun6(setup):
    num1 = 200
    num2 = 30
    assert num1 - num2 == 170
