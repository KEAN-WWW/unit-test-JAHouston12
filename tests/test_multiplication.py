"""Unit tests for the Calculator's multiplication functionality."""
import pytest
from app.calculator import Calculator

@pytest.fixture(name="calc")
def calculator_instance():
    """Fixture to provide a fresh Calculator instance for testing multiplication."""
    return Calculator()

def test_multiply_positive_integers(calc):
    """Test multiplication of two positive integers."""
    assert calc.multiply(6, 7) == 42.0

def test_multiply_by_zero(calc):
    """Test multiplication where one factor is zero."""
    assert calc.multiply(100, 0) == 0.0

def test_multiply_negative_numbers(calc):
    """Test multiplication of two negative numbers."""
    assert calc.multiply(-5, -2) == 10.0
    