import source.shapes as shapes
import pytest

class TestCircle:
    def test_area(self):
        result = shapes.Circle(5).area()
        assert result == 78.5

    def test_perimeter(self):
        result = shapes.Circle(6).perimeter()
        assert result == 37.68


    # parametrized test
    @pytest.mark.parametrize("a,expected", [
        (5, 78.5)
    ])
    def test_param(self,a,expected):
        result = shapes.Circle(a).area()
        assert result == expected 