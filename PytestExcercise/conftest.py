import pytest


@pytest.fixture(scope='class')
def setup():                  # Execute first
    Num = 99
    assert Num==99, "Not equals"
    print("Executed First")
    yield                               # Execute lastly
    print("Executed lastly")

@pytest.fixture(scope='class')
def Data():
    return ["Rajini", "Test123"]  # user name and password

@pytest.fixture(params=["set1", "set2", "set3"])
def runWithMultipleDataSet(request):
    return request.param
