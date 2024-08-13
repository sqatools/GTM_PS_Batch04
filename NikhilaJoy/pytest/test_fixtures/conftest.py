#This is a central fixture file
import pytest
from datetime import datetime

@pytest.fixture(scope="function")
def first_setup1(request):
    with open("testing.log","a") as file:
        file.write(f"\n function name:{request.node.name}")
        file.write(f"{datetime.now()}--function execution started--\n")
    yield
    with open("testing.log","a") as file:
        file.write(f"{datetime.now()}--functionexecution completed--\n")

@pytest.fixture(scope="module",autouse=True)
def module_setup1(request):
    with open("testing.log","a") as file:
        file.write(f"\n module name:{request.node.name}")
        file.write(f"{datetime.now()}--module execution started--\n")
    yield
    with open("testing.log","a") as file:
        file.write(f"{datetime.now()}--module execution completed--\n")
