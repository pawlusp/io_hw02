"""Tests for Calculator Class"""

import pytest
from calculator import Calculator

#Tests
class TestCalculator:
    """Test the Calculator class"""

    def test_sum(self):
        """Check that sum returns the sum of two numbers"""
        assert Calculator(3,5).sum() == 8

    def test_sum_float(self):
        """Check that sum returns the sum of two floats"""
        assert Calculator(3.21,5.34).sum() == pytest.approx(8.55)

    def test_subtract(self):
        """Check that subtract returns the subtract of two numbers"""
        assert Calculator(3,5).subtract() == -2

    def test_subtract_string(self):
        """Check that string returns the typeError"""
        with pytest.raises(TypeError):
            Calculator(3, '5').subtract()

    def test_multiply(self):
        """Check that multiply returns the multiply of two numbers"""
        assert Calculator(3,5).multiply() == 15
        assert Calculator(-3,-5).multiply() == 15
        assert Calculator(3,0).multiply() == 0

    def test_divide(self):
        """Check that divide returns the divide of two numbers"""
        assert Calculator(10,5).divide() == 2

    def test_zero_divide(self):
        """Check that divide by zero returns the ZeroDivisionError"""
        with pytest.raises(ZeroDivisionError):
            Calculator(3,0).divide()

    @pytest.mark.parametrize("a, b, expected", [
            (2, 3, 5),
            (-1, -2, -3),
            (2.5, 3.5, 6.0),
        ])

    def test_add_parametrized(self, a, b, expected):
        """Check multiple sum cases using parametrization"""
        calc = Calculator(a, b)
        assert calc.sum() == expected
