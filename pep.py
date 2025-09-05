"""
    This is for assignment Best Practices 1.1 What is PEP? and 1.2 the Zen of Python
"""

def comparison(first_number, second_number):
  '''
        This function compares two numbers and tells us which is higher
        otherwise tells us the difference between them
  '''
  try:
    if first_number > 0 and second_number > 0:
        # Checks for if both the first and second number are greater the 0
        if first_number > second_number:
        # Checks if the first number is greater then the second number, if it is it prints the first number
            for number in range(second_number):
                print(first_number)
        else:
        # If the first number isn't greater then the second, it will print the second
            for number in range(first_number):
                print(second_number)

    elif first_number == 0 or second_number == 0:
        # Checks if both the first and second numbers are equal to 0
            return "Zero found"
    
    else:
        # Runs if the first and/or second number are less then 0
        # If either condition, it takes the larger number and subtracts the lower number
        if first_number < second_number:
                return first_number - second_number
        else:
                return second_number - first_number
  except TypeError as error:
       print("There was an error.")