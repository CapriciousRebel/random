import random

secret_number = 0
count = 0


def init():
    '''initializes the game variables'''
    global secret_number
    global count

    secret_number = random.randint(0, 100)
    count = 0


def check(number):
    '''checks the guessed number against the secret number'''
    global secret_number
    global count
    count += 1

    if(secret_number == number):
        print("\nCorrect guess!")
        print("You guessed it in " + str(count) + " tries!")
        command = input("Do you wish to play again?(y/n): ")
        if(command == 'y'):
            start_game()
        else:
            exit()

    elif(number > secret_number):
        print("\nYour number is too high!")
        game()
    else:
        print("\nYour number is too low!")
        game()


def game():
    '''play the game'''
    global secret_number

    user_number = int(input("Enter your next guess: "))
    check(user_number)


def start_game():
    '''start the game'''


start_game()
