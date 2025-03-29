# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. 
#         Create a program that do the same functionality without using rindex() function.

# Function to find the index of a substring in a string from the end
def find_rindex(string, substring):
    for i in range(len(string) - len(substring), -1, -1): # Start from the end of the string
        if string[i:i + len(substring)] == substring:
            return i  # Return the index if found
    return None