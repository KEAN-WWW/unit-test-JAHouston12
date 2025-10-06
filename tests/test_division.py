"""Unit tests for the Calculator's division functionality."""
import pytest
from app.calculator import Calculator

@pytest.fixture(name="calc")
def calculator_instance():
    """Fixture to provide a fresh Calculator instance for testing division."""
    return Calculator()

def test_divide_positive_numbers(calc):
    """Test standard division of two positive numbers."""
    assert calc.divide(10, 2) == 5.0

def test_divide_with_float_result(calc):
    """Test division resulting in a non-integer (float) number."""
    assert calc.divide(10, 4) == 2.5

def test_divide_by_zero_raises_error(calc):
    """Test division by zero, ensuring it raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

def test_divide_zero_by_number(calc):
    """Test division of zero by a non-zero number."""
    assert calc.divide(0, 5) == 0.0
    