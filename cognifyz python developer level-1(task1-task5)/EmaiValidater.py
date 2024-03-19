import re

def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Match the pattern against the email address
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    email = input("Enter an email address: ")
    if validate_email(email):
        print("You Have Entered Valid email address.")
    else:
        print("You Have Entered Invalid email address.")

if __name__ == "__main__":
    main()
