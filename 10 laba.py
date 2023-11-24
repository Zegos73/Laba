import tkinter as tk
from tkinter import messagebox
player = "X"
board = [["" for _ in range(3)] for _ in range(3)]


def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Ничья"

    return None

def is_board_full(board):
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def on_button_click(row, col):
    global player

    if board[row][col] == "":
        board[row][col] = player
        buttons[row][col].config(text=player)
        winner = check_winner()
        if winner:
            if winner == "Ничья":
                messagebox.showinfo("Игра окончена", "Ничья!")
            elif winner == "O":
                messagebox.showinfo("Игра окончена", "Победил компьютер!")
            elif winner == "X":
                messagebox.showinfo("Игра окончена", "Победил игрок!")
        else:
            player = "O" if player == "X" else "X"
            if player == "O":
                make_ai_move()

def make_ai_move():
    if not is_board_full(board):
        best_move = get_best_move(board, "O")
        if best_move:
            row, col = best_move
            on_button_click(row, col)
def get_best_move(board, player):
    best_score = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = player
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move
def minimax(board, depth, is_maximizing):
    scores = {"X": -1, "O": 1, "Ничья": 0}
    winner = check_winner()
    if winner:
        return scores[winner]
    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

root = tk.Tk()
root.title("Крестики-нолики")
buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=15, height=7,
                                  command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)
root.mainloop()
