# Prog03. lower() converts all characters of the string into lower case. 
#         Create a program that do the same functionality without using lower() function.

# Prompt user to enter a string
string = input("Enter a string: ")

# Initialize an empty string to store the lowercase version of the input string
lowercase_string = ""

# Iterate through each character in the input string
for char in string:
    if char.isupper(): # Check if the character is uppercase
        lowercase_string += char.swapcase() # Convert the uppercase character to lowercase and add it to the result string
    else:
        lowercase_string += char