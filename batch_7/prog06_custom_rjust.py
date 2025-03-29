# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. 
#         Create a program that do the same functionality without using rjust() function.

# Function to replicate rjust()
def custom_rjust(string, width):
    if width <= len(string):
        return string
    else:    
        spaces = width - len(string) # Calculate the number of spaces needed to reach the desired width
        return ' ' * spaces + string # Add the spaces to the left side of the string