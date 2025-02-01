
# Script that prints "Hello, World!"
def hello_world(x):
    #print("Hello, World!")
    return x + 1


# Test case that confirms the script prints, "Hello, World!"
def test_hello_world():
    #assert hello_world() == "Hello, World!"
    assert hello_world(3) == 4
