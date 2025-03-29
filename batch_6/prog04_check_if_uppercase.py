# Prog04. isupper() check if all characters of the string is on upper case. 
#         Create a program that do the same functionality without using isupper() function.

# Create a function to check if all characters in a string are uppercase
def is_uppercase(string):
    for char in string:
        if char.islower():  # Check if the character is lowercase
            return False
    return True