class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print(f"Addition: {calc.add(5, 3)}")
    print(f"Subtraction: {calc.subtract(10, 4)}")
    print(f"Multiplication: {calc.multiply(6, 7)}")
    print(f"Division: {calc.divide(15, 3)}")

# Hi this indicates custom guidelines working
