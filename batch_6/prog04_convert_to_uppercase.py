# Prog04. isupper() check if all characters of the string is on upper case. 
#         Create a program that do the same functionality without using isupper() function.

# Prompt user to enter a string
string = input("Enter a string: ")

# Initialize an empty string to store the uppercase version of the input string
uppercase_string = ""

# Iterate through each character in the input string
for char in string:
    if char.islower(): # Check if the character is lowercase
        uppercase_string += char.swapcase() # Convert the lowercase character to uppercase and add it to the result string
    else:
        uppercase_string += char