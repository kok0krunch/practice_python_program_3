# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. 
#         Create a program that do the same functionality without using zfill() function.

# Function to replicate zfill()
def custom_zfill(number, width):
    if width <= len(number):
        return number
    else:
        zeros = width - len(number) # Calculate the number of zeros needed to reach the desired width
        return '0' * zeros + number # Add the zeros to the left side of the number

# Prompt user to enter a number and the total width
number = input("Enter a number: ")
width = int(input("Enter the total width of the number: "))

# Apply the custom zfill function
result = custom_zfill(number, width)

# Print the result
print(f"Result: {result}")