import pytest


@pytest.fixture(scope="session")
def emdb():
    print("connect to emdb")
    return "emdb"
