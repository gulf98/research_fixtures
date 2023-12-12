import pytest


@pytest.fixture(scope="session")
def get_artifacts():
    print("get chapaev arifacts")
    return "chapaev"


@pytest.fixture(scope="session")
def run_task_and_get_artifacts():
    print("run task for regression tests")
    return "regression"


pytest_plugins = [
    "fixtures.emdb",
    "fixtures.floors.floors",
    "fixtures.immersive.immersive"
]
