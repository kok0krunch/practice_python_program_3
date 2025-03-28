# Prog05. endswith() check if the string end part matches the function parameter. 
#         Create a program that do the same functionality without using endswith() function.

# Prompt user to enter a string and a suffix to check
string = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

# Function to check if a string ends with a specific substring
def endswith(string, suffix):
    # Compare the end of the string with the suffix
    if string[-len(suffix):] == suffix:
        return True
    else:
        return False
    
# Check if the string ends with the given suffix and print the result
if endswith(string, suffix):
    print("The string ends with:", suffix)
else:
    print("The string DOES NOT end with:", suffix)   