#board display function
import os

def display_board(board):
    os.system('cls') #In Windows
    #In Linux use: os.system('clear')

    print(board[7] + " | ",board[8] + " | ",board[9])
    print("--|----|---")
    print(board[4] + " | ",board[5] + " | ",board[6])
    print("--|----|---")
    print(board[1] + " | ",board[2] + " | ",board[3])
    print("--|----|---")
  
#make a function for players to choose their symbol (X or O) returns a tuple (player1_marker, player2_marker)
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
     
#function for placing the marker on the board 
def place_marker(board, marker, position):
    board[position] = marker
    
#winner check function returns boolean
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
  
#randomize player order returns Player 1 or Player 2 at random
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#check if a space is free returns boolean
def space_check(board, position):
    
    return board[position] == ' '
  
#check if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#make a player decide where to place marker function returns a number after a check if it is occupied
def player_choice(board):
    
    chosen_num = 0
    valid_pos = False
    
    while chosen_num not in range(1,10):
        chosen_num = int(input("Select a valid position from 1 to 9: "))
        valid_pos = space_check(board,chosen_num)
        if valid_pos:
            return chosen_num
        else:
            print("This space is occupied... Choose another one.")
            continue

#play again function returns boolean
def replay():
    
    answer = ""
    
    while answer != "Y" and answer != "N":
        answer = input("Play again? (Y or N): ")
    
    return answer == 'Y'
  
#main game starts here!
while True:  
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
