import os

def print_board(board):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

def is_board_full(board):
    return ' ' not in board

board = [' '] * 9
player = 'X'

while True:
    print_board(board)

    # Get the player's move
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

    # Make the move
    board[move] = player

    # Check for a winner or a tie
    if check_winner(board):
        print_board(board)
        print(f"Player {player} wins!")
        void = input()
        break
    elif is_board_full(board):
        print_board(board)
        print("It's a tie!")
        void = input()
        break

    # Switch to the other player
    player = 'O' if player == 'X' else 'X'
