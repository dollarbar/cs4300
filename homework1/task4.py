# This program exemplifies duck typing.
# The discounting function should return the same value no matter the type.
# Test functions use an integer and a float for two different trials
# asserting the same value.



# function returns final price after discount
def discount_product(product_price, discount):
    return product_price * (1 - discount)


# Test Functions need to test against the exact same value and type

# product_price as integer
def test_discount_with_integer():

    assert discount_product(100, 0.2) == 80


# product_price as float
def test_discount_with_float():

    assert discount_product(100.000, 0.200) == 80





