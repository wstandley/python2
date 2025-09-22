"""
    Module Level Docstring:
    This is for Assignment Best Practices 4.1 PEP 257 Docstring conventions
"""

# Sample Python program without comments and docstrings

class Calculator:
    """
        A class to represent a calculator
    """
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        """This function takes in a value and adds to the value"""
        self.value += num

    def subtract(self, num):
        """This function takes in a value and subtracts from the value"""
        self.value -= num

    def multiply(self, num):
        """This function takes in a value and multiplies the value"""
        self.value *= num

    def divide(self, num):
        """This function takes in a value and divides the value"""
        if num != 0:
            self.value /= num
        else:
            raise ValueError("Cannot divide by zero")

    def clear(self):
        """This method returns the value to 0"""
        self.value = 0

    def get_value(self):
        """This method returns the value"""
        return self.value

def main():
    calc = Calculator() # sets calc to call the Calculator() class for the methods
    calc.add(10)
    calc.subtract(2)
    calc.multiply(5)
    # TODO: Add an input for users to input their own numbers
    try:
        calc.divide(0)
    except ValueError as e:
        print(e)
    calc.divide(4)
    print(f"Final value: {calc.get_value()}")

if __name__ == "__main__":
    main()
