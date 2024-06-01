import pytest

# global fixtures
# defines ones use anytime antwhere

# @pytest.fixture(scope="class") run only before class
@pytest.fixture()
def setup():
    # opening chrome browser or seting up db
    print("I will be first forever")
    # after yeild everything is post executed after test case ran
    yield
    # close browser
    print("I will execute last")

@pytest.fixture()
def loaddata():
    # load data before and pass it to test_func
    # use return
    print("inside load data")
    return [
        "Himanshu", "Goyal", "goyalhimanshu464@gmail.com"
    ]

# incase of return its mandatory to pass fixture name in test_func