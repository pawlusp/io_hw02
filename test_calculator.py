import sys
sys.path.insert(1, '/var/home/student/PycharmProjects/PythonProject/')

from calculator import Calculator
import pytest

#Tests
def test_sum():
    assert Calculator(3,5).sum() == 8

def test_sum_float():
    assert Calculator(3.21,5.34).sum() == pytest.approx(8.55)

def test_substract():
    assert Calculator(3,5).substract() == -2

def test_substract_string():
    with pytest.raises(TypeError):
        Calculator(3, '5').substract()

def test_multiply():
    assert Calculator(3,5).multiply() == 15

def test_divide():
    assert Calculator(10,5).divide() == 2

def test_zero_divide():
    assert Calculator(3,0).divide() == "Błąd: Dzielenie przez zero jest niedozwolone."
