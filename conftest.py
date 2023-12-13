import pkgutil

import pytest

import fixtures


@pytest.fixture(scope="session")
def get_artifacts():
    print("get chapaev arifacts")
    return "chapaev"


@pytest.fixture(scope="session")
def run_task_and_get_artifacts():
    print("run task for regression tests")
    return "regression"


def get_fixture_plugins():
    plugins = []
    prefix = fixtures.__name__ + "."
    for _, module_name, _ in pkgutil.walk_packages(fixtures.__path__, prefix):
        plugins.append(module_name)
    return plugins


pytest_plugins = get_fixture_plugins()

# pytest_plugins = [
#     "fixtures.emdb",
#     "fixtures.floors.floors",
#     "fixtures.immersive.immersive"
# ]
