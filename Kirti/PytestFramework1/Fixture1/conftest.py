from datetime import datetime

import pytest


@pytest.fixture(scope="function", autouse=True)
def first_setup(request):
    with open("execution.log", "a") as file:
        file.write(f"\n test name :{request.node.name}\n ")
        file.write(f"{datetime.now()}-- function execution started --\n")
    yield
    with open("execution.log", "a") as file:
        file.write(f"{datetime.now()}-- function execution completed --\n")

# python -m pytest -v -s .\Fixture1\test_fixture1.py
