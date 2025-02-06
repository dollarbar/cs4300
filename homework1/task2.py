# This program tests for proper data types
# Test functions use function calls with a variable 
# or a simply a variable declared without a function





# Test for type integer - two separate function
def is_integer(x):
    return x

def test_int():
    assert isinstance(is_integer(5), int)





# Test for type float - using variable initialized outside function
value_float = 12.123
def test_float():
    assert isinstance(value_float, float)





# Test for string
value_string = 'asdf'
def test_string():
    assert isinstance(value_string, str)





# Test for boolean
value_boolean = False
def test_boolean():
    assert isinstance(value_boolean, bool)




# Test for list
value_list = ['1',3, [5, 6]]
def test_list():
    assert isinstance(value_list, list)





# Test for dictionary
value_dictionary = {'key1': 'value1', 'key2': 2}
def test_dictionary():
    assert isinstance(value_dictionary, dict)

