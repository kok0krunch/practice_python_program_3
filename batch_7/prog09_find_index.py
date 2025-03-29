# Prog09. index() return the first location of the function parameter in the string. 
#         Create a program that do the same functionality without using index() function.

# Function to find the index of a substring in a string
def find_index(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i  # Return the index if found
    return None