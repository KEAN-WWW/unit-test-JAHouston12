"""Unit tests for the Calculator's subtraction functionality."""
import pytest
from app.calculator import Calculator

@pytest.fixture(name="calc")
def calculator_instance():
    """Fixture to provide a fresh Calculator instance for testing subtraction."""
    return Calculator()

def test_subtract_positive_numbers(calc):
    """Test basic subtraction resulting in a positive number."""
    assert calc.subtract(10, 3) == 7.0

def test_subtract_resulting_in_negative_number(calc):
    """Test subtraction resulting in a negative number."""
    assert calc.subtract(3, 10) == -7.0

def test_subtract_with_zero(calc):
    """Test subtraction from zero."""
    assert calc.subtract(0, 5) == -5.0
    