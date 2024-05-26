
# pytest -v -s
# -s for logs
# -v for verbose
# start file and function name with test_
# if same method names it will override
#  py.test to run all test cases
# py.test -k CreditCard run only creditcard named test cases

def test_firstProgram():
    print("Hello world")

def test_secondProgram():
    a = 12

    assert a == 23, "test failed woho!"