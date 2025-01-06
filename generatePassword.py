import random
import string


def generate_password(length=12):
    if length < 8 or length > 16:
        raise ValueError(
            "Password length must be between 8 and 16 characters.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#%^&*()"

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from all character sets
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)


# Generate a password with a random length between 8 and 16
password_length = random.randint(8, 16)
password = generate_password(password_length)
print("Generated Password:", password)
