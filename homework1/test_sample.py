import pytest
# Learning from freecodecamp
# Use *_test or test_* for file names



### Rich assertion introspection

### Support parameterized and fixture-based testing


# . means pass

def add(number_one, number_two):
    return number_one + number_two

def divide(number_one, number_two):
    return number_one / number_two

def test_add():
    result = add(1, 4)
    assert result == 5

# assert tests a condition

def test_divide():
    result = divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = divide(10, 0)
    

def test_divide_by_zero_again():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# Strings

def test_add_strings():
    result = add("i like ", "burgers")
    assert result == "i like burgers"



