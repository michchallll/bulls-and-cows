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

def evaluate_guess(secret, guess):
    """Vyhodnotí tip uživatele a vrátí počet bulls a cows."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows

def main():
    """Hlavní logika hry Bulls and Cows."""
    print(
        f"Hi there!\n"
        f"{'-' * 47}\n"
        f"I've generated a random 4 digit number for you.\n"
        f"Let's play a bulls and cows game.\n"
        f"{'-' * 47}\n"
        f"Enter a number:\n"
        f"{'-' * 47}"
    )

    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()
    
    while True:
        guess = input(">>> ")
        print("-" * 47)
        
        if not is_valid_guess(guess):
            print(
                f"Invalid input! Enter a 4-digit number with unique digits.\n"
                f"{'-' * 47}"
            )
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print(
                f"Correct, you've guessed the right number\nin {attempts} guesses!\n"
                f"Time taken: {duration} seconds\n"
                f"{'-' * 47}"
            )
            
            if attempts <= 5:
                print("Outstanding performance!!! 🔥")
            elif attempts <= 10:
                print("Amazing performance! 🎉")
            elif attempts <= 15:
                print("Average performance. 👍")
            else:
                print("Not so good, better luck next time. 😅")
            break

        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"
        print(
            f"{bulls} {bull_text}, {cows} {cow_text}\n"
            f"{'-' * 47}"
        )

if __name__ == "__main__":
    main()