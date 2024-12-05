import tkinter as tk
from tkinter import messagebox

# Fonction pour vérifier s'il y a un gagnant
def check_victory(board):
    # Vérification des lignes
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    # Vérification des colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

# Fonction pour vérifier si la grille est pleine (égalité)
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Fonction Minimax avec profondeur limitée
def minimax(board, depth, is_maximizing, max_depth):
    if check_victory(board):
        return 1 if not is_maximizing else -1
    if is_board_full(board) or depth >= max_depth:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False, max_depth)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True, max_depth)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

# Fonction pour le meilleur coup de l'IA avec une profondeur limitée
def best_move(board, max_depth):
    best_score = -float('inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(board, 0, False, max_depth)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

# Fonction pour gérer le délai avant de jouer le coup de l'IA
def delayed_ai_move(board, buttons, max_depth):
    root.after(2000, ai_move, board, buttons, max_depth)  # 2000 ms = 2 secondes

# Fonction pour gérer le clic sur la grille
def player_move(row, col, board, buttons, max_depth):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        buttons[row][col].config(text='X')  # Le bouton affiche 'X'
        if check_victory(board):
            messagebox.showinfo("Victoire", "Le joueur X a gagné!")
            disable_buttons(buttons)
        elif is_board_full(board):
            messagebox.showinfo("Égalité", "Match nul!")
            disable_buttons(buttons)
        else:
            delayed_ai_move(board, buttons, max_depth)  # Délai avant que l'IA joue

# Fonction pour l'IA
def ai_move(board, buttons, max_depth):
    move = best_move(board, max_depth)
    if move:
        row, col = move
        board[row][col] = 'O'
        buttons[row][col].config(text='O')  # L'IA affiche 'O'
        if check_victory(board):
            messagebox.showinfo("Victoire", "L'IA (O) a gagné!")
            disable_buttons(buttons)
        elif is_board_full(board):
            messagebox.showinfo("Égalité", "Match nul!")
            disable_buttons(buttons)

# Fonction pour désactiver tous les boutons après la fin du jeu
def disable_buttons(buttons):
    for row in buttons:
        for button in row:
            button.config(state='disabled')

# Fonction pour réinitialiser la grille
def reset_game(board, buttons, max_depth):
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '
            buttons[row][col].config(text=' ')  # Réinitialise le texte des boutons
            buttons[row][col].config(state='normal')  # Réactive les boutons

# Fonction pour créer la fenêtre de jeu
def create_game_window():
    global root  # Déclare 'root' comme global pour l'utiliser dans d'autres fonctions
    root = tk.Tk()
    root.title("Tic Tac Toe - IA (Minimax)")

    board = [[' ' for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]
    max_depth = 3  # Profondeur maximale de l'IA (plus faible = IA moins forte)

    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                                          command=lambda r=row, c=col: player_move(r, c, board, buttons, max_depth))
            buttons[row][col].grid(row=row, column=col)

    reset_button = tk.Button(root, text="Réinitialiser", font=('normal', 20), command=lambda: reset_game(board, buttons, max_depth))
    reset_button.grid(row=3, column=0, columnspan=3)

    root.mainloop()

# Démarrer le jeu
create_game_window()
