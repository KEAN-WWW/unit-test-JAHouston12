"""Unit tests for the Calculator's addition functionality."""
import pytest
from app.calculator import Calculator

@pytest.fixture(name="calc")
def calculator_instance():
    """Fixture to provide a fresh Calculator instance for testing addition."""
    return Calculator()

def test_add_two_positive_integers(calc):
    """Test addition of two simple positive integers."""
    assert calc.add(5, 3) == 8.0

def test_add_positive_and_negative_integer(calc):
    """Test addition involving a positive and a negative integer."""
    assert calc.add(10, -4) == 6.0

def test_add_with_float_numbers(calc):
    """Test addition of floating-point numbers."""
    assert calc.add(2.5, 1.3) == pytest.approx(3.8)
