import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    print("welcome to guess the number game !")
    print("I have picked a number between 1 and 100 try to guess it ?")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too High! Try again.")
        else:
            print("congractulations! Youguess the number. ")
guess_the_number()
