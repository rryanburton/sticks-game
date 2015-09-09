# sticks.py
header = '\n/-\-\-/-\-/\-/\-/-/-\/-/\-//-/\-\n'
def main():
    '''acts as the default function.
    Greets the player and starts the game-mode()
    '''
    print(header)
    print('\n\nWelcome to the Game of Sticks!\n\n')
    game_mode()

def game_mode():
    '''asks user to choose between human or computer
    opponent
    '''
    print(header)
    print('\nPlay against a friend (1)')
    print('or')
    print('Play against the computer (2)\n')
    opponent = input("Which option do you take (1-2)?\n")
    if opponent == '1':
        print('\nPrepare to compete against a Real person.\n')
        gameloop()
    elif opponent == '2':
        print('\nPretend you are the computer!\n')
        gameloop()
    else:
        game_mode()

def gameloop():
    '''asks for inital stick count.
    shows stick count
    asks player 1 for play.
    checks that play.
    shows stick count
    asks player 2 for play.
    checks that play.
    '''
    turn = 'player 1'
    while True:
        print(header)
        stick_count = int(input('How many sticks do you want (10-100)? '))
        if 10 <= stick_count <= 100:
            # return stick_count
            break
        else:
            print('\nYou will have to try again.\n')
            gameloop()
    print(stick_count)


    # while True:
    #     while stick_count > 0:
    #         if stick_count > 1:
    #             print("\nThere are currently {} sticks on the board. \n".format(stick_count))
    #             break
    #         else:
    #             print("\nThe game is over. {} lost.".format(turn))
    #             playagain = input('Do you want to play again? ')
    #             if playagain == 'y':
    #                 gameloop()
    #             else:
    #                 main()

    player1_choice = input('Player 1: How many sticks do you take (1-3)? ')
    if player1_choice is '1':
        stick_count -= 1
    elif player1_choice is '2':
        stick_count -= 2
    elif player1_choice is '3':
            stick_count -= 3
    print(stick_count)
    exit()
#
# def playagain():
#     response = input('Do you want to play again?')
#     if response is 'y':
#         exit()
#     else:
#         print('thanks for playing.')
#         exit()
#



# while stick_count > -1:
#     turn = 'player 1'
#     stick_counter()
#
#
#     # print(stick_count)
#     turn = 'player 2'
#     stick_counter()
#     player2_choice = input('Player 2: How many sticks do you take (1-3)? ')
#     if player2_choice is '1':
#         stick_count -= 1
#     elif player2_choice is '2':
#         stick_count -= 2
#     elif player2_choice is '3':
#         stick_count -= 3
#     # print(stick_count)
# # player_turn()


if __name__ == '__main__':
    main()
