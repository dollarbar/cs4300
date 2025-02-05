

# discounting
def discount_product(product_price, discount):
    return product_price * (1 - discount)

def test_discount_product():
    # final product price should be integer
    assert discount_product(100, 0.2) == 80

def test_discount_product_float():
    # final product price should be float
    assert discount_product(100.1234, 0.234) == 76.6945244



