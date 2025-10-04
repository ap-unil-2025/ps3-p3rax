"""
Bonus Challenge: Password Generator
Generate secure passwords with customizable options.
"""

import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_digits=True, use_special=True):
    """
    Generate a random password based on criteria.

    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters

    Returns:
        str: Generated password
    """
    characters = ""

    # Build character set based on parameters
    pools=[]
    if use_lowercase:
        characters +=string.ascii_lowercase
        pools.append(string.ascii_lowercase)
    if use_uppercase:
        characters +=string.ascii_uppercase
        pools.append(string.ascii_uppercase)
    if use_digits:
        characters +=string.digits
        pools.append(string.digits)
    if use_special:
        characters +=string.punctuation
        pools.append(string.punctuation)

    if not characters:
        return "Error: No character types selected!"

    password = []

    # Ensure at least one character from each selected type
    password=[random.choice(pool) for pool in pools]

    # Fill the rest of the password randomly
    remaining=max(0, length - len(password))
    password +=[random.choice(characters) for _ in range(remaining)]

    # Shuffle the password list to randomize order
    random.shuffle(password)

    return ''.join(password)


def password_strength(password):
    """
    Rate password strength from 1-5.

    Args:
        password (str): Password to evaluate

    Returns:
        str: Strength rating
    """
    score = 0

    # Add points for different criteria
    # - Length >= 8: +1 point
    if len(password) >= 8:
        score +=1
    # - Length >= 12: +1 point
    if len(password) >= 12:
        score +=1
    # - Contains lowercase: +1 point
    if any(c.islower() for c in password):
        score +=1
    # - Contains uppercase: +1 point
    if any(c.isupper() for c in password):
        score +=1
    # - Contains digits: +1 point
    if any(c.isdigit() for c in password):
        score +=1
    
    if any(c in string.punctuation for c in password):
        score +=1

    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return strength[min(score, 5)]


def main():
    """Main function to run the password generator."""
    print("Password Generator")
    print("-" * 30)

    # Get password length from user
    length_input = input("Password length (default 12): ").strip()
    length = int(length_input) if length_input else 12

    # Generate password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")

    # Generate alternative passwords
    print("\nAlternative passwords:")
    for i in range(3):
        alt_password = generate_password(length)
        print(f"{i+1}. {alt_password} ({password_strength(alt_password)})")


if __name__ == "__main__":
    main()