# Prog04. islower() check if all characters of the string is on lower case. 
#         Create a program that do the same functionality without using islower() function.

# Create a function to check if all characters in a string are lowercase
def is_lowercase(string):
    for char in string:
        if char.isupper():  # Check if the character is uppercase
            return False
    return True

# Prompt user to enter a string
string = input("Enter a string: ")