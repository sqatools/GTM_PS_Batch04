import pytest

from datetime import datetime


@pytest.fixture(scope='function')
def first_setup(request):
    with open ("execution.log","a") as file:
        file.write(f"\n testcase level : {request.node.name}\n")
        file.write("\nexecution started\n")
    yield
    with open ("execution.log","a") as file:
        file.write("\nexecution completed\n")


@pytest.fixture(scope='module', autouse=True)
def module_setup(request):
    with open ("execution.log","a") as file:
        file.write(f"\n module name : {request.node.name}\n")
        file.write(f"\n {datetime.now()}---module execution started\n")
    yield
    with open ("execution.log","a") as file:
        file.write(f"\n {datetime.now()}-- module execution completed\n")
