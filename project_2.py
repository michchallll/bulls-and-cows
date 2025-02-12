"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michael Kubát
email: michchallll@gmail.com
discord: michchallll
"""

import random
import time

def generate_secret_number():
    """Generuje náhodné 4místné číslo s unikátními číslicemi a nezačínající nulou."""
    digits = list(range(1, 10))  # První číslo nesmí být 0
    random.shuffle(digits)
    secret = [str(digits.pop(0))]  # První číslo
    digits.append(0)  # Přidá 0 do seznamu čísel
    random.shuffle(digits)
    secret.extend(str(digits.pop()) for _ in range(3))
    return ''.join(secret)

def is_valid_guess(guess):
    """Ověří, zda je vstup validní (4 unikátní číslice, nezačíná 0, pouze čísla)."""
    return (
        len(guess) == 4 and
        guess.isdigit() and
        len(set(guess)) == 4 and
        guess[0] != '0'
    )

def main():
    """Hlavní logika hry Bulls and Cows."""
    print(
        f"Hi there!\n"
        f"{'-' * 47}\n"
        f"I've generated a random 4 digit number for you.\n"
        f"Let's play a bulls and cows game.\n"
        f"{'-' * 47}"
    )

    secret_number = generate_secret_number()
    print(secret_number)




if __name__ == "__main__":
    main()