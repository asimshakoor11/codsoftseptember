



import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/\\"

    if length < 8:
        charset = lowercase_letters + digits
    else:
        charset = lowercase_letters + uppercase_letters + digits + special_characters

    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
