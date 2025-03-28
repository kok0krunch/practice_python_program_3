# Prog08. swapcase() reverse the casing of each of the character of the string.
#         Create a program that do the same functionality without using swapcase() function.

# Function to replicate swapcase()
def custom_swapcase(string):
    swapped_string = ""  # Initialize an empty string to store the swapped characters
    for char in string:
        if char.islower():  # Check if the character is lowercase and convert it to uppercase
            swapped_string += char.upper()
        elif char.isupper():  # Check if the character is uppercase and convert it to lowercase
            swapped_string += char.lower()
        else:
            swapped_string += char  # Keep the character as is if it's not a letter
    return swapped_string