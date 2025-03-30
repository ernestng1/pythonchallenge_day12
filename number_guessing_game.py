from art import logo
import random

def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    random_number_chosen = random.choice(range(1,101))
    EASY_ATTEMPT = 10
    HARD_ATTEMPT = 5
    if difficulty == "easy":
        number_guessing_game_sub(EASY_ATTEMPT, random_number_chosen)
    elif difficulty == "hard":
        number_guessing_game_sub(HARD_ATTEMPT, random_number_chosen)

def number_guessing_game_sub(number,random_number):
    print(f"You have {number} attempts remaining to guess the number.")
    correct_guess = False
    i = 0
    while i < number  and correct_guess == False:
        guess = int(input("Make a guess: "))
        i += 1
        if guess > random_number:
            print("Too high.\nGuess again.")
            print(f"You have {number - i} attempts remaining to guess the number.")
        elif guess < random_number:
            print("Too low.\nGuess again.")
            print(f"You have {number - i} attempts remaining to guess the number.")
        else:
            print("You guessed correctly! You win!")
            correct_guess = True
    if correct_guess == False:
        print("You've run out of guesses. You lose!")
        print(f"The correct number is {random_number}")
        number_guessing_game()
    else:
        number_guessing_game()

number_guessing_game()