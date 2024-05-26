import pytest

# pytest -v -s
# -s for logs
# -v for verbose
# start file and function name with test_
# if same method names it will override
#  py.test to run all test cases
# py.test -k CreditCard run only creditcard named test cases
# grouping and tagging
    # pytest -m snoke -v -s
    # @pytest.mark.smoke smoke is the tag name
# to skip a test case
    # @pytest.mark.skip
# test will run but not report
    # @pytest.mark.xfail
# fixtures -> run something before executing testcase
    # @pytest.fixture()
    # yield

@pytest.fixture()
def setup():
    # opening chrome browser or seting up db
    print("I will be executing first")
    # after yeild everythin is post executed after test case ran
    yield
    # close browser
    print("I will exectute last")

def test_fixtureDemo(setup):
    print("i will execute steps after")

@pytest.mark.xfail
def test_failButExec():
    str = "hi"
    assert str == "huii", "test failed"

@pytest.mark.smoke
def test_firstProgram():
    print("Hello world")

@pytest.mark.skip
def test_secondProgram():
    a = 12

    assert a == 23, "test failed woho!"