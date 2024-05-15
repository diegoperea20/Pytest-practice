import source.shapes as shapes
import pytest

# fixture decorator for my_rectangle
@pytest.fixture
def my_rectangle():
   return shapes.Rectangle(5, 10)

def test_area(my_rectangle):
    assert my_rectangle.area() == 50

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 30

