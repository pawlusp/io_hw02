"""Tests for Calculator Class"""
import sys
sys.path.insert(1, '/var/home/student/PycharmProjects/PythonProject/')

from calculator import Calculator
import pytest

#Tests
def test_sum():
    """Chech that sum returns the sum of two numbers"""
    assert Calculator(3,5).sum() == 8

def test_sum_float():
    """Chech that sum returns the sum of two floats"""
    assert Calculator(3.21,5.34).sum() == pytest.approx(8.55)

def test_substract():
    """Chech that substract returns the substract of two numbers"""
    assert Calculator(3,5).substract() == -2

def test_substract_string():
    """Chech that string returns the typeError"""
    with pytest.raises(TypeError):
        Calculator(3, '5').substract()

def test_multiply():
    """Chech that multiply returns the multiply of two numbers"""
    assert Calculator(3,5).multiply() == 15

def test_divide():
    """Chech that divide returns the divide of two numbers"""
    assert Calculator(10,5).divide() == 2

def test_zero_divide():
    """Chech that divide by zero returns the error message"""
    assert Calculator(3,0).divide() == "Błąd: Dzielenie przez zero jest niedozwolone."
