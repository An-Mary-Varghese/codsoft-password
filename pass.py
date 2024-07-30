import random
import string

def generate_password(length=12, include_symbols=True):
    """
    Generate a random password.

    Parameters:
    - length (int): Length of the password.
    - include_symbols (bool): Whether to include symbols in the password.

    Returns:
    - str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")

    # Define character sets
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to handle user input and generate password."""
    try:
        length = int(input("Enter the desired length of the password: "))
        include_symbols = input("Include symbols (Y/N)? ").strip().lower() == 'y'

        # Generate the password
        password = generate_password(length, include_symbols)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
