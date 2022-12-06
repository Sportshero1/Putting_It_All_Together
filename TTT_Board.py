# # creating the board
# def ttt_board():
#     print()
#     print('This is your Tic-Tac-Toe board:\n')
#     a = (' ___' * 3)
#     b = '   '.join('||||')
#     print('\n'.join((a,b,a,b,a,b,a, )))
#     print()

# ttt_board()

# Create codes for inputting the user choices
def mark_choice():
    print()
    a = ('___' * 4)
    row = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(a)
    print(row[0],' |', row[1],' |',row[2])
    print(a)
    print(row[3],' |', row[4],' |',row[5])
    print(a)
    print(row[6],' |', row[7],' |',row[8])

mark_choice()


# Give the options for the players to choose if they would like to go first and the option of their mark
def player_choice():
    players = ''
    player1 = ''
    player2 = ''
    while players not in ('Y', 'N'):
        players = input("player-1 would like to go first? ")
        players = players.upper()
        if player_choice not in ('Y', 'N'):
            print("Invalid Entry. Try Again!")
        else:
            pass
    if players == 'Y':
        while player1 not in ('X', 'O'):
            player1 = input("Select your mark for player 1. X or O: ")
            player1 = player1.upper()
            if player1 not in ('X', 'O'):
                print("Invalid Entry. Try Again")
            else:
                pass
    else:
        while player2 not in ('X', 'O'):
            player2 = input("Select your mark for player 2. X or O: ")
            player2 = player2.upper()
            if player2 not in ('X', 'O'):
                print("Invlaid Entry. Try Again")
            else:
                pass
    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'
    elif player2 == 'X':
        player1 = 'O'
    elif player2 =='O':
        player1 = 'X'
    print(f'Mark for Player 1 is: {player1} and Mark for Player 2 is: {player2}')
    return player1, player2

# player_choice()

