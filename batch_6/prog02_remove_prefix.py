# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
#         Create a program that do the same functionality without using removeprefix() function.

# Prompt user to enter a string and a prefix to remove
string = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

# Remove the prefix from the string (if it exists at the beginning)
result = string.replace(prefix, "", 1)  # Replace the first occurrence of the prefix with an empty string

print("String after removing the prefix:", result)