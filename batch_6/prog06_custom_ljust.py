# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
#         Create a program that do the same functionality without using ljust() function.

# Function to replicate ljust()
def custom_ljust(string, spaces):
    if spaces > 0:
        return string + ' ' * spaces # Add the spaces to the end of the string
    else:
        return string
    
# Prompt user to input a string and number of spaces to add
string = input("Enter a string: ")
spaces = int(input("Enter number of spaces to input at the end: "))

# Apply the custom ljust function
result = custom_ljust(string, spaces)

# Print the result
print(f"String after applying custom ljust: '{result}'")