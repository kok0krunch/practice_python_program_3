# Prog05. startswith() check if the string beginning part matches the function parameter. 
#         Create a program that do the same functionality without using startswith() function.

# Function to check if a string starts with a specific substring
def startswith(string, prefix):
    if string[:len(prefix)] == prefix: # Compare the start of the string with the prefix
        return True
    else:
        return False

# Prompt user to enter a string and a prefix to check
string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")