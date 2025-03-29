# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. 
#         Create a program that do the same functionality without using capitalize() function.

# Prompt user to input a string
string = input("Enter a string: ")

# Create a function to replicate capitalize()
def custom_capitalize(string):
    # Check if the string is empty
    if not string:
        return string
    # Capitalize the first letter and lower the rest
    return string[0].upper() + string[1:].lower()

# Apply the custom capitalize function
result = custom_capitalize(string)

# Print the result
print(result)