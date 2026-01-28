import random

guess_number = random.randint(1, 100)
tries = 5

print("🎯 Welcome to the Guessing Game!")
print("You have 5 tries to guess the number between 1 and 100.\n")

while tries > 0:
        user_guess = int(input("Enter your guess: "))

        if user_guess < 1 or user_guess > 100:
            print("Please guess a number between 1 and 100.\n")
        elif user_guess > guess_number:
            tries -= 1
            print(f"Too high! You have {tries} trie(s) left.\n")
        elif user_guess < guess_number:
            tries -= 1
            print(f"Too low! You have {tries} trie(s) left.\n")
        elif user_guess == guess_number:
            print("Congratulations! You guessed the correct number!")
        else:
            print("Invalid input. Please enter a number.\n")
            break
if tries == 0:
    print("💀 Game Over! You've used all your tries.")
    print("✅ The correct number was:", guess_number)





