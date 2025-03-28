# lstrip() remove the space characters at the beginning of the string. 
# Create a program that do the same functionality without using lstrip() function.

string = input("Enter a string with leading spaces: ")

# Remove leading spaces using a loop
while len(string) > 0 and string[0] == ' ':
    string = string[1:]  # Remove the first character if it's a space

print(string)