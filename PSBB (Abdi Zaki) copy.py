from collections import Counter

def can_form_palindrome(s):
    # Count the frequency of each character
    char_count = Counter(s)
    
    # Count the number of characters with odd frequency
    odd_count = sum(count % 2 for count in char_count.values())
    
    # Return True if there's at most one character with odd frequency
    return odd_count <= 1

# Test the function
input_string = input("Enter a string: ")
if can_form_palindrome(input_string):
    print("Yes, it's possible to rearrange the characters to form a palindrome!")
else:
    print("No, it's not possible to rearrange the characters to form a palindrome.")
