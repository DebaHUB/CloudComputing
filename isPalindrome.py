def is_palindrome(input_str):
    # Convert input to lowercase (for case-insensitive comparison)
    input_str = str(input_str).lower()
    
    # Remove spaces (for phrases and sentences)
    input_str = ''.join(input_str.split())

    # Compare the original input with its reverse
    return input_str == input_str[::-1]

# Get input from the user
user_input = input("Enter a word or number: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")
