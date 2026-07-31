import random

number = random.randint(1, 100)

difficulty = input(
    "Choose difficulty:\n"
    "1. Easy (10 tries)\n"
    "2. Medium (7 tries)\n"
    "3. Hard (5 tries)\n"
    "Enter your choice: "
)

if difficulty == "1":
    attempts = 10
elif difficulty == "2":
    attempts = 7
elif difficulty == "3":
    attempts = 5
else:
    print("Invalid choice. Defaulting to Hard level.")
    attempts = 5

while attempts > 0:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < number:
        print("Too Low!")
    else:
        print("Too High!")

    attempts -= 1
    print("Remaining attempts:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The correct number was", number)