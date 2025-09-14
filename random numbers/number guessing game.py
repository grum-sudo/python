import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("python number guessing game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("input is your guess? ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("out of bounds")
            print(f"select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("too low try again")
        elif guess > answer:
            print("too high try again")
        else:
            print(f"you guessed it the answer was {answer}")
            print(f"it took you {guesses} guesses")
            is_running = False
    else:
        print("Invalid input. Please enter a number")
        print(f"select a number between {lowest_num} and {highest_num}")
