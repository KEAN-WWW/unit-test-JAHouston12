"""
app/calculator.py: Contains the Calculator class for basic arithmetic.
"""

class Calculator:
    """
    Represents a simple calculator object capable of basic math operations.
    """

    def add(self, num1: float, num2: float) -> float:
        """Adds two numbers."""
        return num1 + num2

    def subtract(self, num1: float, num2: float) -> float:
        """Subtracts the second number from the first."""
        return num1 - num2

    def multiply(self, num1: float, num2: float) -> float:
        """Multiplies two numbers."""
        return num1 * num2

    def divide(self, num1: float, num2: float) -> float:
        """
        Divides the first number by the second.

        Raises:
            ZeroDivisionError: If the divisor (num2) is zero.
        """
        if num2 == 0:
            # This is the line that fixes the test failure!
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

