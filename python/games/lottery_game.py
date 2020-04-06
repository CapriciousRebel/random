import random

count = 0
tries = 0
secret_numbers = []
user_guesses = []


print("Welcome to the lottery game!")
n = int(input("For how many numbers do you want to play this game? "))
for i in range(n):
    secret_numbers.append(random.randint(0, 49))

freq_secret = {}
for number in secret_numbers:
    if number in freq_secret:
        freq_secret[number] += 1
    else:
        freq_secret[number] = 1

print("I have picked " + str(n) + " random numbers from 0 to 49")
print("Your task is to guess all of them: ")

while True:

    count = 0
    tries += 1
    user_guesses = []

    for i in range(n):
        user_input = int(input("\nEnter guess number: "))
        user_guesses.append(user_input)

    freq_guesses = {}

    for guess in user_guesses:
        if guess in freq_guesses:
            freq_guesses[guess] += 1
        else:
            freq_guesses[guess] = 1

    for guess, guess_count in freq_guesses.items():
        if guess in freq_secret:
            count += 1
            freq_secret[guess] -= 1

    if(count != n):
        print("Your guesses: ")
        print(user_guesses)
        print("You guessed " + str(count) + " numbers correctly, Try again!")
    else:
        print("Secret numbers: ")
        print(secret_numbers)
        print("Your guesses: ")
        print(user_guesses)
        print("you win in " + str(tries) + " attempts!" )
        break

