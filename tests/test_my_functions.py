import source.my_functions as my_functions
import pytest

def test_add():
    result = my_functions.add(5, 10) 
    assert result == 15

def test_subtract():
    result = my_functions.subtract(5, 10) 
    assert result == -5

def test_multiply():
    result = my_functions.multiply(5, 10)
    assert result == 50

def test_divide():
    result = my_functions.divide(5, 10)
    assert result == 0.5

# expected error
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(5, 0)

#test strings
def test_add_string():
    result = my_functions.add("Hello ", "World")
    assert result == "Hello World"


# parametrized test
@pytest.mark.parametrize("a, b, expected", [
    (5, 10, 15),
    (5, 5, 10),
    (10, 5, 15),
])
def test_add_param(a, b, expected):
    result = my_functions.add(a, b)
    assert result == expected


# skip test 
@pytest.mark.skip(reason="no way of currently testing this")
def test_add_skip():
    result = my_functions.add(5, 10) 
    assert result == 15