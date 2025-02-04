# This program writes a simple hello world script by a function return value and uses pytest
# to test the function. A successful test means the hello world function returns "Hello, World!".
# To apply pytest to this file, it must be named test_*.py or *_test.py
# Also, the function used for testing needs to be named test_*():


# Script that prints "Hello, World!"
def hello_world():
    my_string = "Hello, World!"
    return my_string
    


# Test case that confirms the script prints, "Hello, World!"
def test_hello_world():
    assert hello_world() == "Hello, World!"

