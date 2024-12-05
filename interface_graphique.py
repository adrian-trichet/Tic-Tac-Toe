import tkinter as tk
import random
from tkinter import messagebox

# Function to center the window on the screen
def center_window(window, width, height):
    """
    Centers the window of the application on the screen.
    
    Parameters:
        window (tk.Tk): The Tkinter window to be centered.
        width (int): The width of the window.
        height (int): The height of the window.
    """
    screen_width = window.winfo_screenwidth()  # Get the width of the screen
    screen_height = window.winfo_screenheight()  # Get the height of the screen
    position_top = int(screen_height / 2 - height / 2)  # Calculate the top position
    position_right = int(screen_width / 2 - width / 2)  # Calculate the left position
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')  # Set window geometry

# Function to start the game based on the selected mode
def start_game():
    mode = mode_var.get()  # Récupérer le mode sélectionné (IA facile, IA difficile ou 2 joueurs)
    root.destroy()  # Fermer la fenêtre de sélection
    if mode == "IA Facile":
        play_game(True, "facile")  # Mode IA facile
    elif mode == "IA Difficile":
        play_game(True, "difficile")  # Mode IA difficile
    else:
        play_game(False, "")  # Mode 2 joueurs

# Fonction qui gère la logique du jeu
def play_game(is_ai_mode, ai_level):
    """
    Initializes and starts the Tic Tac Toe game.
    
    Parameters:
        is_ai_mode (bool): If True, AI plays against the player.
        ai_level (str): The AI difficulty level ("easy").
    """
    # Create the game window
    game_root = tk.Tk()
    game_root.title("Tic Tac Toe")
    game_root.resizable(False, False)
    
    # Centrer la fenêtre
    center_window(game_root, 500, 500)

    current_player = 'X'  # Le joueur commence avec 'X'
    buttons = []
    grid = [[' ' for _ in range(3)] for _ in range(3)]  # Matrice pour l'état du jeu

    message_label = tk.Label(game_root, text="", font=("Arial", 20))
    message_label.grid(row=3, column=0, columnspan=3)

    def disable_buttons():
        """Disables all buttons after the game ends."""
        for row in buttons:
            for button in row:
                button.config(state="disabled")

    def button_click(row, col):
        """
        Handles button clicks in the grid, updates the game state,
        and checks for victory.
        
        Parameters:
            row (int): The row of the clicked button.
            col (int): The column of the clicked button.
        """
        nonlocal current_player
        if buttons[row][col]['text'] != " ":
            return  # Ignore click if the button is already occupied
        buttons[row][col].config(text=current_player)
        grid[row][col] = current_player
        victory, message = check_victory(grid)
        if victory:
            messagebox.showinfo("Game Over", message)
            disable_buttons()
            return
        if all(cell != ' ' for row in grid for cell in row):
            message_label.config(text="Égalité !")
            disable_buttons()
            return
        current_player = 'O' if current_player == 'X' else 'X'  # Switch players
        if is_ai_mode and current_player == 'O':
            ai_move(ai_level)

    def check_victory(grid):
        """
        Checks if there is a winner.
        
        Parameters:
            grid (list): The matrix representing the game state.
        
        Returns:
            tuple: A boolean indicating if a victory was detected,
                   and a victory or non-victory message.
        """
        # Check rows
        for row in grid:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True, f"Le joueur avec '{row[0]}' a gagné (ligne)."
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
                return True, f"Le joueur avec '{grid[0][col]}' a gagné (colonne)."
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
            return True, f"Player '{grid[0][0]}' wins (diagonal)."
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
            return True, f"Le joueur avec '{grid[0][2]}' a gagné (diagonale)."
        return False, "Pas encore de victoire."

    def ai_move(level):
        # Ajouter un délai de 500ms avant que l'IA joue
        game_root.after(500, make_ai_move, level)

    def make_ai_move(level):
        if level == "facile":
            easy_ai_move()
        else:
            hard_ai_move()  # Appelle la version améliorée de l'IA difficile

    def easy_ai_move():
        available_moves = [(r, c) for r in range(3) for c in range(3) if grid[r][c] == ' ']
        if available_moves:
            move = random.choice(available_moves)
            button_click(move[0], move[1])

    def available_moves(board):
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

    def minimax(board, depth, is_maximizing, alpha, beta):
        winner, _ = check_victory(board)
        if winner == 'X':  # 'X' perd
            return -1
        elif winner == 'O':  # 'O' gagne
            return 1
        if all(cell != ' ' for row in board for cell in row):  # égalité
            return 0
        
        if is_maximizing:
            max_eval = -float('inf')
            for move in available_moves(board):
                board[move[0]][move[1]] = 'O'  # L'IA joue
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[move[0]][move[1]] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in available_moves(board):
                board[move[0]][move[1]] = 'X'  # Le joueur humain joue
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[move[0]][move[1]] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def hard_ai_move():
        best_move = None
        best_value = -float('inf')
        for move in available_moves(grid):
            grid[move[0]][move[1]] = 'O'  # L'IA joue
            move_value = minimax(grid, 0, False, -float('inf'), float('inf'))  # Recherche du meilleur coup
            grid[move[0]][move[1]] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = move
        button_click(best_move[0], best_move[1])

    def create_buttons():
        """
        Creates the buttons for the Tic Tac Toe grid.
        """
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(game_root, text=" ", font=("Arial", 50), width=5, height=2,
                                   command=lambda r=row, c=col: button_click(r, c))
                button.grid(row=row, column=col, sticky="nsew")  # Utilisation de grid pour une disposition flexible
                button_row.append(button)
            buttons.append(button_row)

        # Assurer que les cellules de la grille sont redimensionnables
        for i in range(3):
            game_root.grid_columnconfigure(i, weight=1)
            game_root.grid_rowconfigure(i, weight=1)

    create_buttons()
    game_root.mainloop()

# Interface de sélection de mode
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

# Centrer la fenêtre
center_window(root, 500, 500)

mode_var = tk.StringVar()
mode_var.set("2 Joueurs")

# Radiobutton pour 2 joueurs
tk.Radiobutton(root, text="2 Joueurs", variable=mode_var, value="2 Joueurs", font=("Arial", 20)).pack()

# Radiobutton pour IA facile
tk.Radiobutton(root, text="Jouer contre l'IA facile", variable=mode_var, value="IA Facile", font=("Arial", 20)).pack()

# Radiobutton pour IA difficile
tk.Radiobutton(root, text="Jouer contre l'IA difficile", variable=mode_var, value="IA Difficile", font=("Arial", 20)).pack()

# Bouton de démarrage
start_button = tk.Button(root, text="Commencer le jeu", font=("Arial", 20), command=start_game)
start_button.pack(pady=150)

root.mainloop()  # Start the mode selection window
