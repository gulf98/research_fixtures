import pytest


@pytest.fixture(scope="session", autouse=True)
def get_object1(emdb):
    print("create get_object1")
    assert emdb == "emdb"
    yield "object1"
    print("delete get_object1")
