import pytest
import math

# continued from test_sample.py

class Shape:

    def area(self):

        pass

    def perimeter(self):

        pass

class Circle(Shape):


    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected 

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    # added during fixtures examples
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False

        return self.width == other.width and self.length == other.length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)


@pytest.fixture
def my_rectangle():
    return Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return Rectangle(5, 6)


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
