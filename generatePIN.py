import random

def is_valid_pin(pin):
    # Check if the pin is a number pattern
    if pin in ["012345", "123456", "234567", "345678", "456789", "567890", "678901", "789012"]:
        return False

    # Check for three consecutive digits
    for i in range(len(pin) - 2):
        if pin[i] == pin[i + 1] == pin[i + 2]:
            return False

    return True

def generate_random_pin():
    while True:
        # Generate a random 6-digit PIN
        pin = ''.join(random.choices('0123456789', k=6))
        if is_valid_pin(pin):
            return pin

# Generate a valid PIN
pin = generate_random_pin()
print("Generated PIN:", pin)