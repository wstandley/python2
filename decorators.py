"""
    This is for assignment OOP 2.4 Decorators
"""

import time

class TimingDecorator:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Start Recording time of function
        start_time = time.time()
        result = self.func(*args, **kwargs) # Call factorial()
        end_time = time.time() # end recording time
        execution_time = end_time - start_time # calculate execution time
        print(f"Execution time of {self.func.__name__}: {execution_time:.6f} seconds")
        return result


@TimingDecorator
def factorial(number):
    """
        This function passes through the number given and calculates its factorial
    """
        
    if number == 0:
        return 1

    result = 1

    while number > 0:
        result = result * number
        number = number - 1
    return result


factorial(10)
