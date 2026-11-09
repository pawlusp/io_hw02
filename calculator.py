"""A simple calculator module"""

class Calculator:
    """Calculator class"""
    def __init__(self, op1: float, op2: float):
        """Initializer class"""
        self.op1 = op1
        self.op2 = op2
    def sum(self) -> float:
        """Add two numbers"""
        return self.op1 + self.op2
    def substract(self) -> float:
        """Subtract two numbers"""
        return self.op1 - self.op2
    def multiply(self) -> float:
        """Multiply two numbers"""
        return self.op1 * self.op2
    def divide(self):
        """Divide two numbers"""
        try:
            return self.op1 / self.op2
        except ZeroDivisionError:
            return "Błąd: Dzielenie przez zero jest niedozwolone."
