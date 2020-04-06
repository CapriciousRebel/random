import random

print("Rules: if a player rolls a 6, then that player gets to roll again.\n")
player1 = input("Enter player1's name: ")
player2 = input("Enter player2's name: ")
player1_score = 0
player2_score = 0
again = ''


def roll_die():
    '''returns the output of a single die roll'''
    return random.randint(1, 6)


def show_scores():
    print("\nScores: \n    " + player1 + ": " + str(player1_score) +
          "\n    " + player2 + ": " + str(player2_score))


def player1_play():
    global player1
    global player1_score
    global again

    print("\nIt's " + player1 + "'s turn!" + again)
    command = input("Roll die?(y/n): ")

    if(command == 'y'):
        number = roll_die()

        print(player1 + " rolled: " + str(number))
        player1_score += roll_die()

        if player1_score >= 100:
            print("\n" + player1 + " wins the game !")
            show_scores()
            exit()

        if(number == 6):
            again = " again!"
            player1_play()

    elif(command == 'n'):
        print(player1 + " didn't roll the die!")
    else:
        print("Invalid command!")


def player2_play():
    global player2
    global player2_score
    global again

    print("\nIt's " + player2 + "'s turn!" + again)
    command = input("Roll die?(y/n): ")

    if(command == 'y'):
        number = roll_die()
        print(player2 + " rolled: " + str(number))
        player2_score += roll_die()

        if player2_score >= 100:
            print("\n" + player2 + " wins the game !")
            show_scores()
            exit()

        if(number == 6):
            again = " again!"
            player2_play()

    elif(command == 'n'):
        print(player2 + " didn't roll the die!")
    else:
        print("Invalid command!")


while True:
    again = ''
    player1_play()
    player2_play()
    show_scores()
