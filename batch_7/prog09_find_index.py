# Prog09. index() return the first location of the function parameter in the string. 
#         Create a program that do the same functionality without using index() function.

# Function to find the index of a substring in a string
def find_index(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i  # Return the index if found
    return None

# Prompt user to enter a string and a substring to find its index
string = input("Enter a string: ")
substring = input("Enter the substring to find its index: ")

# Apply the custom index function
result = find_index(string, substring)

# Print the result
if result is None:
    print("Not found in string")
else:
    print(f"The index of '{substring}' in the string is: {result}")