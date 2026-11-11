"""Tests for Calculator Class"""

import pytest
from calculator import Calculator

#Tests
def test_sum():
    """Check that sum returns the sum of two numbers"""
    assert Calculator(3,5).sum() == 8

def test_sum_float():
    """Check that sum returns the sum of two floats"""
    assert Calculator(3.21,5.34).sum() == pytest.approx(8.55)

def test_substract():
    """Check that substract returns the substract of two numbers"""
    assert Calculator(3,5).substract() == -2

def test_substract_string():
    """Check that string returns the typeError"""
    with pytest.raises(TypeError):
        Calculator(3, '5').substract()

def test_multiply():
    """Check that multiply returns the multiply of two numbers"""
    assert Calculator(3,5).multiply() == 15
    assert Calculator(-3,-5).multiply() == 15
    assert Calculator(3,0).multiply() == 0

def test_divide():
    """Check that divide returns the divide of two numbers"""
    assert Calculator(10,5).divide() == 2

def test_zero_divide():
    """Check that divide by zero returns the ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        Calculator(3,0).divide()
