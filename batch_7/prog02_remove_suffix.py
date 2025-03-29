# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. 
#         Create a program that do the same functionality without using removesuffix() function.

# Prompt user to enter a string and a prefix to remove
string = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

# Remove the suffix from the string (if it exists at the ending)
result = string.replace(suffix, "", -1) # Replace the first occurrence of the suffix with an empty string