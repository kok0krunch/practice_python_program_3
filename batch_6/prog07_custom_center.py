# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. 
#         Create a program that do the same functionality without using center() function.

# Function to replicate center()
def custom_center(string, width):
    if width <= len(string):
        return string
    
    # Calculate the number of spaces to add
    spaces = width - len(string) 
    
    # Calculate the number of spaces to add for the left and right sides
    left_spaces = spaces // 2 
    right_spaces = spaces - left_spaces 
    
    # Add the spaces to the left and right sides of the string
    return ' ' * left_spaces + string + ' ' * right_spaces

# Input from the user
string = input("Enter a string: ")
width = int(input("Enter the total width: "))

# Apply the custom center function
result = custom_center(string, width)