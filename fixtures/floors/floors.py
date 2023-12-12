import pytest


@pytest.fixture(scope="session", autouse=True)
def get_floor1(emdb):
    print("create floor1")
    assert emdb == "emdb"
    yield "floor1"
    print("delete floor1")


@pytest.fixture(scope="session", autouse=True)
def get_floor2(emdb):
    print("create floor2")
    assert emdb == "emdb"
    yield "floor2"
    print("delete floor2")
