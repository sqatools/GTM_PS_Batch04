# This is central fixture file
import pytest
from datetime import datetime


@pytest.fixture(scope="function")
def first_setup(request):
    with open("execution.log", "a") as file:
        file.write(f"\n test name :{request.node.name}\n ")
        file.write(f"{datetime.now()}-- function execution started --\n")
    yield
    with open("execution.log", "a") as file:
        file.write(f"{datetime.now()}-- function execution completed --\n")


@pytest.fixture(scope="module", autouse=True)
def module_setup(request):
    with open("execution.log", "a") as file:
        file.write(f"\n module name :{request.node.name}\n")
        file.write(f"{datetime.now()} -- module execution started --\n")
    yield
    with open("execution.log", "a") as file:
        file.write(f"{datetime.now()}-- module execution completed --\n")
