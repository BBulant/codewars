""" 
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""

def create_phone_number(n):
    numstring = ""
    for digit in n:
        # All digits within the given list of integers get converted into a single string of numbers
        numstring += str(digit)
    # Formatting the final phone number string by using an F-string 
    phone_number = f"({numstring[0:3]}) {numstring[3:6]}-{numstring[6:]}"
    return phone_number