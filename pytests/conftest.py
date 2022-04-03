import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last ")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["cherry","sricharan","Chuchu","jayshree"]


@pytest.fixture(params=["chrome","Firefox","IE"])
def crossbrowsers(request):
    return request.param
