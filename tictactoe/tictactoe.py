import tkinter as tk
from tkinter import messagebox

def print_board():
    for i in range(9):
        buttons[i].config(text=board[i])

def check_winner(board):
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

def make_move(index):
    global player
    if board[index] == ' ':
        board[index] = player
        print_board()
        if check_winner(board):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            window.quit()
        elif is_board_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            window.quit()
        player = 'O' if player == 'X' else 'X'
    else:
        messagebox.showwarning("Invalid Move", "This spot is already taken.")

def create_buttons():
    for i in range(9):
        button = tk.Button(window, text=' ', width=10, height=3, command=lambda i=i: make_move(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

window = tk.Tk()
window.title("Tic-Tac-Toe")

board = [' '] * 9
player = 'X'
buttons = []

create_buttons()
print_board()

window.mainloop()
