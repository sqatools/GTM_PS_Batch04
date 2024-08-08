
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
    print("\n -------test execution started----\n")
    yield
    print("--------test execution completed----------\n")

@pytest.fixture(scope='module',autouse=True)
def setup_module():
    print("\n----module execution started-------\n")
    yield
    print("\n----module exeution completed ")

@pytest.fixture(scope='package',autouse=True)
def setup_package():
    print("\n -----package execution strted--------")
    yield
    print("\n----------package level execution completed-------------")

@pytest.fixture(scope='session',autouse=True)
def setup_session():
    print("\n ---- session execution started---------")
    yield
    print("\n----session execution completed------\n")


def test_addition(setup):
    num1=10
    num2=20
    assert num1+num2==30

def test_multiplication(setup):
    num1=30
    num2=20
    assert num1 * num2 ==500

