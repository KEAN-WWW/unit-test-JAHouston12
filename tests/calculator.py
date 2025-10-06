"""
tests/test_calculator.py
Unit tests for the completed Calculator class.
"""
import pytest
# The import path MUST be correct relative to the project root
from app.calculator import Calculator


# Fixture to provide a Calculator instance to tests
@pytest.fixture(name="calc")
def calculator_instance():
    """
    Returns a fresh instance of the Calculator class for each test.
    """
    return Calculator()


# --- Addition Tests ---

def test_add_two_positive_integers(calc):
    """Test addition of two simple positive integers."""
    assert calc.add(5, 3) == 8


def test_add_positive_and_negative_integer(calc):
    """Test addition involving a positive and a negative integer."""
    assert calc.add(10, -4) == 6


def test_add_with_float_numbers(calc):
    """Test addition of floating-point numbers for precision."""
    assert calc.add(2.5, 1.3) == pytest.approx(3.8)


def test_add_with_zero(calc):
    """Test addition with zero."""
    assert calc.add(42, 0) == 42


# --- Subtraction Tests ---

def test_subtract_positive_numbers(calc):
    """Test basic subtraction resulting in a positive number."""
    assert calc.subtract(10, 3) == 7


def test_subtract_resulting_in_negative_number(calc):
    """Test subtraction resulting in a negative number."""
    assert calc.subtract(3, 10) == -7


def test_subtract_with_zero(calc):
    """Test subtraction from zero."""
    assert calc.subtract(0, 5) == -5


def test_subtract_two_negative_numbers(calc):
    """Test subtraction of a negative number from a negative number."""
    assert calc.subtract(-5, -2) == -3  # -5 - (-2) = -3


# --- Multiplication Tests ---

def test_multiply_positive_integers(calc):
    """Test multiplication of two positive integers."""
    assert calc.multiply(6, 7) == 42


def test_multiply_by_zero(calc):
    """Test multiplication where one factor is zero."""
    assert calc.multiply(100, 0) == 0


def test_multiply_negative_numbers(calc):
    """Test multiplication of two negative numbers (should be positive)."""
    assert calc.multiply(-5, -2) == 10


def test_multiply_mixed_signs(calc):
    """Test multiplication of a positive and a negative number."""
    assert calc.multiply(4, -3) == -12


# --- Division Tests ---

def test_divide_positive_numbers(calc):
    """Test standard division of two positive numbers."""
    assert calc.divide(10, 2) == 5


def test_divide_with_float_result(calc):
    """Test division resulting in a non-integer (float) number."""
    assert calc.divide(10, 4) == pytest.approx(2.5)


def test_divide_negative_numerator(calc):
    """Test division with a negative numerator."""
    assert calc.divide(-10, 2) == -5


def test_divide_by_zero_raises_error(calc):
    """
    Test division by zero, ensuring it raises a specific ValueError exception.
    """
    # pytest.raises checks that the specific exception is thrown
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)


def test_divide_zero_by_number(calc):
    """Test division of zero by a non-zero number (should be 0)."""
    assert calc.divide(0, 5) == 0

