import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("Congratulations! You guessed the number!")
elif guess < number:
    print("Too Low!")
else:
    print("Too High!")