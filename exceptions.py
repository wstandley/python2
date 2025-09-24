"""
    This is for Assignment OOP 3.1 Advanced Exceptions
"""

class TryDividingZero(Exception): # Name appropriately for what I want it to be an error for
    pass

class CantDivideByZero(Exception): # Name appropriately for what I want it to be an error for
    pass

def first_try(number):
    """
        This function tries to divide by zero
        excepts ZeroDivisionError and raises
        custom error: CantDivideByZero
    """
    try:
        try:
            result = number/0
        except ZeroDivisionError:
            raise TryDividingZero("You tried dividing by zero")
    except TryDividingZero as e:
        raise CantDivideByZero("You can't divide by zero") from e
    
    
# Out Try Block
try:  
    first_try(5)  
except CantDivideByZero as e:  
    print("Second Custom Exception:", e)  # Pulls Second Custom Exception
    print("Cause of error:", e.__cause__)  # Pulls First Custom Exception
    print("Context of error:", e.__context__) # Also Pulls First Custom Exception since the ZeroDivisionError gets handled by TryDividingZero

