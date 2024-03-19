def is_palindrome(s):
    # Remove spaces and punctuation, and convert to lowercase for case-insensitive comparison
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the string with its reverse
    return s == s[::-1]

def main():
    user_input = input("Enter a word or phrase to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
