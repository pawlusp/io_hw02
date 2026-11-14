"""A simple calculator module"""

class Calculator:
    """Calculator class"""
    def __init__(self, op1: float, op2: float):
        """Initializer class"""
        self.__op1 = op1
        self.__op2 = op2
    def sum(self) -> float:
        """Add two numbers"""
        return self.__op1 + self.__op2
    def subtract(self) -> float:
        """Subtract two numbers"""
        return self.__op1 - self.__op2
    def multiply(self) -> float:
        """Multiply two numbers"""
        return self.__op1 * self.__op2
    def divide(self) -> float | None:
        """Divide two numbers"""
        if self.__op2 == 0:
            return None
        return self.__op1 / self.__op2

if __name__ == "__main__": #pragma: no cover
    calc = Calculator(5, 6)
    print("Calculator(5, 6):")
    print("Sum:", calc.sum())
    print("Subtract:", calc.subtract())
    print("Multiply:", calc.multiply())
    print("Divide:", calc.divide())
    print("Calculator(5, 0).divide():",Calculator(5, 0).divide())
