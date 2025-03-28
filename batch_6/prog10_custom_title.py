# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
#         Create a program that do the same functionality without using title() function.

# Function to replicate title()
def custom_title(string):
    words = string.split()
    # Capitalize the first letter of each word
    for i in range(len(words)):
        words[i] = words[i][0].upper() + words[i][1:].lower()
    # Join the words back together
    return ' '.join(words)

# Prompt user to input a string
string = input("Enter a string: ")

# Apply the custom title function
result = custom_title(string)

# Print the result
print(result)