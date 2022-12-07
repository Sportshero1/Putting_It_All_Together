# # creating the board idea
# def ttt_board():
#     print()
#     print('This is your Tic-Tac-Toe board:\n')
#     a = (' ___' * 3)
#     b = '   '.join('||||')
#     print('\n'.join((a,b,a,b,a,b,a, )))
#     print()

# ttt_board()

# Create codes for inputting the user choices
def ttt_board():
    print()
    print('See your board, and the options you can choose!')
    a = ('___' * 4)
    row = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(a)
    print(row[0],' |', row[1],' |',row[2])
    print(a)
    print(row[3],' |', row[4],' |',row[5])
    print(a)
    print(row[6],' |', row[7],' |',row[8])

ttt_board()

def mark_choice(choice, marker):
    print()
    player1, player2 = choice
    row = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    i = 1
    while i < 10:
        j = 0
        p = 0
        print(f'This is turn: {i}')
        while j not in row:
            j = input("Player-1: Select position (1-9) for your mark: ")
            if j not in row:
                print("That is an invalid choice. Please try again")
            else:
                pass
        x = row.index(j)
        row.pop(x)
        j = int(j)
        marker[j] = player1
        ttt_board(marker)
        i += 1
        gw = game_winner(choice,marker)
        if gw ==1:
            print("The Winner of the game is Player 1!")
            break
        print(f'It took {i} turns')
        if i == 10:
            break

        while p not in row:
            p = input("Player-1: Select position (1-9) for your mark: ")
            if p not in row:
                print("That is an invalid choice. Please try again")
            else:
                pass
        y = row.index(p)
        row.pop(y)
        p = int(p)
        marker[p] = player2
        ttt_board(marker)
        i += 1
        gw = game_winner(choice,marker)
        if gw == 2:
            print("The Winner of the game is Player 2!")
            break
        print(f'It took {i} turns')
        if i == 10:
            break     
    return marker 

mark_choice()

def game_winner(choice,user_marks):
    player1, player2 = choice
    m = 0
    if user_marks[0] == user_marks[1] == user_marks[2] == player1:
        m = 1
        return m
    elif user_marks[0] == user_marks[3] == user_marks[6] == player1:
        m = 1
        return m
    elif user_marks[0] == user_marks[4] == user_marks[8] == player1:
        m = 1
        return m
    elif user_marks[3] == user_marks[4] == user_marks[5] == player1:
        m = 1 
        return m
    elif user_marks[6] == user_marks[7] == user_marks[8] == player1:
        m = 1
        return m
    elif user_marks[1] == user_marks[4] == user_marks[7] == player1:
        m = 1
        return m
    elif user_marks[2] == user_marks[5] == user_marks[8] == player1:
        m = 1
        return m
    elif user_marks[2] == user_marks[4] == user_marks[6] == player1:
        m = 1
        return m
    elif user_marks[0] == user_marks[1] == user_marks[2] == player2:
        m = 2
        return m
    elif user_marks[0] == user_marks[3] == user_marks[6] == player2:
        m = 2
        return m
    elif user_marks[0] == user_marks[4] == user_marks[8] == player2:
        m = 2
        return m
    elif user_marks[3] == user_marks[4] == user_marks[5] == player2:
        m = 2 
        return m
    elif user_marks[6] == user_marks[7] == user_marks[8] == player2:
        m = 2
        return m
    elif user_marks[1] == user_marks[4] == user_marks[7] == player2:
        m = 2
        return m
    elif user_marks[2] == user_marks[5] == user_marks[8] == player2:
        m = 2
        return m
    elif user_marks[2] == user_marks[4] == user_marks[6] == player2:
        m = 2
        return m
    else:
        m = 3
        return m

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

