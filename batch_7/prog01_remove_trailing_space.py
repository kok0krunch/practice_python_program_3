# Prog01. rstrip() remove the space characters at the end of the string. 
#         Create a program that do the same functionality without using rstrip() function.

# Prompt user to input a string with trailing spaces
string = input("Enter a string with trailing spaces: ")

# Remove trailing spaces using a loop
while len(string) > 0 and string[-1] == ' ':  # Check if the last character is a space
        string = string[:-1]  # Remove the last character
        
# Print the modified string without trailing spaces
print(f"String without trailing spaces: '{string}'")       