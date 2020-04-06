# create two global data-structures
# players is the dictionary with {jersey_number: rating}
# jersey_numbers is the sorted list of jersey numbers
players = {}
jersey_numbers = []


def showMenu():
    '''prints the menu to the output'''

    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("Choose an option: ")


# A function that will call other functions based on the user's command
def command_handler():
    '''handles the given command'''

    # Run an infinite for-loop
    while True:
        # On each iteration, we show the menu and wait for the user input
        showMenu()
        command = input("")

        #  we call the relevant function, based off on the user's command
        if command == 'o':
            output_roster()
        elif command == 'a':
            add_player()
        elif command == 'd':
            delete_player()
        elif command == 'u':
            update_player_rating()
        elif command == 'r':
            output_players_above_rating()
        # when the user enters 'q', the loop breaks, and the program ends
        elif command == 'q':
            break


# this function is called first inside the main() function
# It takes the initial data about the five players
def init():
    '''prompt the user to input five pairs of numbers'''

    # Use the 'global' keyword in each function, to access the global data structures
    global jersey_numbers
    global players

    # run a for-loop 5 times
    for i in range(5):

        # take the user input for the jersey number and rating of each player
        jersey_number = int(input(f"Enter player {i+1}'s jersey number: "))
        rating = int(input(f"Enter player {i+1}'s rating: "))

        # insert into the players dictionary, and jersey_numbers list
        players[jersey_number] = rating
        jersey_numbers.append(jersey_number)

    # finally sort the list, and save it
    jersey_numbers = sorted(jersey_numbers)


# this function prints the current roster
def output_roster():
    '''prints the current ROSTER to the output'''

    global jersey_numbers
    global players

    # Use a for-loop to print all the player's data
    # the key 'jersey_number' is accessed from the jersey_numbers list
    # to obtain the sorted jersey_numbers
    print("\nROSTER")
    for i in range(len(players)):
        jersey_number = jersey_numbers[i]
        print(
            f"Jersey number: {jersey_number}, Rating: {players[jersey_number]}")


# this function adds a new player to the ROSTER
def add_player():
    '''adds a player to the ROSTER'''

    global jersey_numbers
    global players

    # take the user input for the jersey number and rating of the new player
    jersey_number = int(input("\nEnter a new player's jersey number: "))
    rating = int(input("Enter the player's rating: "))

    # insert into the players dictionary, and jersey_numbers list
    players[jersey_number] = rating
    jersey_numbers.append(jersey_number)

    # finally sort the list, and save it
    jersey_numbers = sorted(jersey_numbers)


# this function removes a player from the ROSTER
def delete_player():
    '''removes a player from the ROSTER'''

    global jersey_numbers
    global players

    # take the user input for the jersey number of the new player
    jersey_number = int(input("\nEnter a jersey number: "))

    # delete the player from the players dictionary
    del players[jersey_number]

    # remove the jersey number from the jersey_numbers list
    jersey_numbers.remove(jersey_number)

    # finally sort the list, and save it
    jersey_numbers.sort()


# This function updates the rating of a current player
def update_player_rating():
    '''updates the rating of a player'''

    global jersey_numbers
    global players

    # take the user input for the jersey number and new rating of the existing player
    jersey_number = int(input("\nEnter a jersey number: "))
    new_rating = int(input("Enter a new rating for player: "))

    # update the rating of the player in the players dictionary
    players[jersey_number] = new_rating


# this function outputs the players having a rating above a given rating
def output_players_above_rating():
    '''prints the players having a rating above a given rating'''

    global jersey_numbers
    global players

    # take the user input for the minimun rating
    min_rating = int(input("\nEnter a rating: "))

    # create a list to store the jersey numbers who have a rating above the minimun rating
    above_rating_jersey_numbers = []

    # iterate over the players dictionary, and store the jersey numbers of the players who have
    # rating above the minimun rating
    for jersey_number, rating in players.items():
        if rating > min_rating:
            above_rating_jersey_numbers.append(jersey_number)

    # sort the list, and save it
    above_rating_jersey_numbers = sorted(above_rating_jersey_numbers)

    # Use a for-loop to print all the eligible player's data
    # the key 'jersey_number' is accessed from the above_rating_jersey_numbers
    # to obtain the sorted jersey_numbers
    print(f"ABOVE {min_rating}")
    for jersey_number in above_rating_jersey_numbers:
        print(
            f"Jersey number: {jersey_number}, Rating: {players[jersey_number]}")


# this function is called at the start of the program
def main():
    '''driver function, start point of the code execution'''
    global jersey_numbers
    global players

    # we first call the init() function to take the first 5 player's data
    init()
    # then we ouput the ROSTER
    output_roster()
    # finally we call the command_handler to proceed
    command_handler()


# This is where the execution begins, and we call the main() function first
main()
