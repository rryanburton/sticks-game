# sticks.py
print('Welcome to the Game of Sticks!\n')

stick_count = str(input('How many sticks are there on the table initially (10-100)?'))

print('Play against a friend (1)')
print('or')
print('Play against the computer (2)')
opponent = input("Which option do you take (1-2)?")

stick_count = 12

def game_loop(stick_count, opponent):
    pass

def stick_counter():
    while stick_count > 0:
        if stick_count == 1:
            print("The last stick is on the board.")
        elif stick_count > 1:
            print("There are {} sticks on the board.".format(stick_count))

def player_turn():
    player1_choice = input('Player 1: How many sticks do you take (1-3)?')
    if player1_choice is '1':
        stick_count -= 1
    elif player1_choice is '2':
        stick_count -= 2
    elif player1_choice is '3':
        stick_count -= 3

    player2_choice = input('Player 2: How many sticks do you take (1-3)?')
    if player2_choice is '1':
        stick_count -= 1
    elif player2_choice is '2':
        stick_count -= 2
    elif player2_choice is '3':
        stick_count -= 3


# There are 7 sticks on the board.

# Player 2: How many sticks do you take (1-3)? 3

# There are 5 sticks on the board.
# Player 1: How many sticks do you take (1-3)? 3
#
# There are 2 sticks on the board.
# AI selects 2.
# AI loses.
# Play again (y/n)? y
