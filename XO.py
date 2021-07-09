#Function that prints out the game board
def display_board(board):
    
    print("\n" * 5)
    print(' '+ board[7] + ' |  ' + board[8] + '  | ' + board[9])
    print('---|-----|---')
    print(' '+ board[4] + ' |  ' + board[5] + '  | ' + board[6])
    print('---|-----|---')
    print(' '+ board[1] + ' |  ' + board[2] + '  | ' + board[3])
    


#Function that takes in a player input 
#and assign their marker as 'X' or 'O'
def player_input():
    '''
    Output is in the form of a tuple.
    (Player1_marker, Player2_marker)
    Use tuple unpacking
    '''
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
    #Another logic
    #while marker != 'X' and marker != 'O':
        
        marker = input("Player 1 Choose X or O: ").upper()
        if marker != 'X' and marker != 'O':
            
            print("Invalid Input")
    if marker == 'X':

        return ('X','O')
    else:

        return ('O','X')

    #return (player1, player2)



#Function that takes in the board, 
#a player marker ('X' or 'O'), and a desired position (numbers 1-9) 
#and assigns it to the board
def place_marker(board, marker, position):
    
    board[position] = marker



#Function that takes in a board and a marker (X or O) 
#and then checks to see if that mark has won
def win_check(board,marker):
    #Check 3 rows, 3 columns, 2 diagonals and 
    #see if the markers match
    
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker) or
    (board[1] == board[5] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker))



#Function to randomly decide which player goes first
import random
def coin_flip():
    
    flip = random.randint(0,1)
    if flip:
        return 'Player 2'
    else:
        return 'Player 1'



#Function that returns a boolean indicating whether a space on the board 
#is freely available
def space_check(board,position):
    return board[position] == ' '



#Function that checks if the board is full 
#and returns a boolean value. True if full, False otherwise
def board_full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            #Board not full
            return False
    else:
        #Board full
        return True



#Function that asks for a player's next position (as a number 1-9) 
#and then uses the Function from above to check if it's a free position. 
#If it is, then return the position for later use
def player_choice(board):
    
    position = 0
    while position not in list(range(1,10)) or not space_check(board,position):

        position = input("Choose a position (1-9): ")
        if not position.isdigit():
            
            print("Invalid Input")
            continue
        else:

            position = int(position)

        if position not in list(range(1,10)) or not space_check(board,position):
            print("Invalid Input")
    
    return position



#Function that asks the player if they want to play again 
#and returns a boolean True if they do want to play again
def play_again():

    choice = input("Do you want to play ? Y or N ").upper()

    return choice == 'Y'



#Main
print("\t\tTIC TAC TOE")

#WHILE loop to keep the game running
while True:

    #Game starts
    #Set up Board, Markers, Who goes first
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    print(player1_marker, end = "    ")
    print(player2_marker)
    print("P1, P2")
    turn = coin_flip()
    print(f"{turn} will play first")
    play_game = input("Ready to play? Y or N: ").upper()
    if play_game == 'Y':

        game_on = True
    else:

        game_on = False
    #Gameplay
    while game_on:

        if turn == 'Player 1':
            
            #Display Board
            display_board(board)
            #Choose a position
            print(f"{player1_marker}'s turn")
            position = player_choice(board)
            #Place the marker on the position
            place_marker(board,player1_marker,position)
            #Check if they won
            if win_check(board,player1_marker):

                display_board(board)
                print("Congratulations!!")
                print("Player 1 has won!")
                game_on = False
                #Or check if there is a tie
            else:

                if board_full_check(board):

                    display_board(board)
                    print("Game is Tie")
                    #break
                    game_on = False
                else:

                    #No tie and no win? Then turn of next player
                    turn = 'Player 2'
        else:

            #Player 2 turn
            #Display Board
            display_board(board)
            #Choose a position
            print(f"{player2_marker}'s turn")
            position = player_choice(board)
            #Place the marker on the position
            place_marker(board,player2_marker,position)
            #Check if they won
            if win_check(board,player2_marker):

                display_board(board)
                print("Congratulations!!")
                print("Player 2 has won!")
                game_on = False
                #Or check if there is a tie
            else:

                if board_full_check(board):

                    display_board(board)
                    print("Game is Tie")
                    #break
                    game_on = False
                else:

                    #No tie and no win? Then turn of next player
                    turn = 'Player 1'

    #Break out of the while loop on play_again()
    if not play_again():

        break













'''


board = ['#','X','X','X','O','O','O','X','O','O']
display_board(board)
#print(space_check(board,9))
print(board_full_check(board))

#print(f"{coin_flip()} will play first")




board = ['#','X','O','X','O','O','O','X','O','X']
display_board(board)
x = win_check(board,'O')
print(x)


#Main
#board_main = ['#','X','O','X','O','X','O','X','O','X']
board = [' '] * 10
display_board(board)
player1_marker, player2_marker = player_input()
print(player1_marker, end = "    ")
print(player2_marker)
print("P1, P2")
place_marker(board,'$',5)
display_board(board)
'''