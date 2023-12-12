import pytest


@pytest.fixture(scope="session")
def dgdat_db(get_artifacts):
    print("create dgdat connection")
    assert get_artifacts == "chapaev"
    return "dgdat"
