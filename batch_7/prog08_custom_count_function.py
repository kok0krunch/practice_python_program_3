# Prog08. count() return how many time the function parameter appear in the string. 
#         Create a program that do the same functionality without using count() function.

# Function to count occurrences of a substring in a string
def custom_count(string, substring):
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) # Find the substring starting from the current position
        if start == -1: # If not found, break the loop
            break
        count += 1 # Increment the count if found
        start += len(substring) # Move to the end of the found substring
    return count