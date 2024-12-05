import tkinter as tk
import random

# Fonction pour centrer la fenêtre sur l'écran
def center_window(window, width, height):
    """
    Centre la fenêtre de l'application sur l'écran.
    
    Parameters:
        window (tk.Tk): La fenêtre Tkinter à centrer.
        width (int): La largeur de la fenêtre.
        height (int): La hauteur de la fenêtre.
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Fonction pour démarrer le jeu en fonction du mode sélectionné
def start_game():
    """
    Récupère le mode sélectionné (IA facile ou 2 joueurs)
    et lance la fonction de jeu correspondante.
    """
    mode = mode_var.get()  # Récupère le mode sélectionné
    root.destroy()  # Ferme la fenêtre de sélection
    if mode == "IA Facile":
        play_game(True, "facile")  # Mode IA facile
    else:
        play_game(False, "")  # Mode 2 joueurs

# Fonction principale qui gère la logique du jeu
def play_game(is_ai_mode, ai_level):
    """
    Initialise et démarre le jeu Tic Tac Toe.
    
    Parameters:
        is_ai_mode (bool): Si True, l'IA joue contre le joueur.
        ai_level (str): Le niveau de difficulté de l'IA ("facile").
    """
    # Création de la fenêtre de jeu
    game_root = tk.Tk()
    game_root.title("Tic Tac Toe")
    game_root.resizable(False, False)  # Désactive le redimensionnement de la fenêtre
    
    # Centrer la fenêtre
    center_window(game_root, 500, 500)

    current_player = 'X'  # Le joueur commence avec 'X'
    buttons = []  # Liste pour stocker les boutons de la grille
    grid = [[' ' for _ in range(3)] for _ in range(3)]  # Matrice pour l'état du jeu

    # Label pour afficher les messages de victoire ou d'égalité
    message_label = tk.Label(game_root, text="", font=("Arial", 20))
    message_label.grid(row=3, column=0, columnspan=3)

    def disable_buttons():
        """Désactive tous les boutons après la fin de la partie."""
        for row in buttons:
            for button in row:
                button.config(state="disabled")

    def button_click(row, col):
        """
        Gère les clics sur les boutons de la grille, met à jour l'état du jeu
        et vérifie la victoire.
        
        Parameters:
            row (int): La ligne du bouton cliqué.
            col (int): La colonne du bouton cliqué.
        """
        nonlocal current_player
        if buttons[row][col]['text'] != " ":
            return  # Ignore le clic si le bouton est déjà occupé
        buttons[row][col].config(text=current_player)
        grid[row][col] = current_player
        victory, message = check_victory(grid)
        if victory:
            message_label.config(text=message)
            disable_buttons()
            return
        if all(cell != ' ' for row in grid for cell in row):  # Vérifie si la grille est pleine
            message_label.config(text="Égalité !")
            disable_buttons()
            return
        current_player = 'O' if current_player == 'X' else 'X'  # Change de joueur
        if is_ai_mode and current_player == 'O':
            ai_move(ai_level)

    def check_victory(grid):
        """
        Vérifie s'il y a un gagnant.
        
        Parameters:
            grid (list): La matrice représentant l'état du jeu.
        
        Returns:
            tuple: Un booléen indiquant si une victoire a été détectée,
                   et un message de victoire ou de non-victoire.
        """
        # Vérifie les lignes
        for row in grid:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True, f"Le joueur avec '{row[0]}' a gagné (ligne)."
        # Vérifie les colonnes
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
                return True, f"Le joueur avec '{grid[0][col]}' a gagné (colonne)."
        # Vérifie les diagonales
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
            return True, f"Le joueur avec '{grid[0][0]}' a gagné (diagonale)."
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
            return True, f"Le joueur avec '{grid[0][2]}' a gagné (diagonale)."
        return False, ""  # Aucun gagnant pour l'instant

    def ai_move(level):
        """
        Gère le mouvement de l'IA avec un délai.
        
        Parameters:
            level (str): Le niveau de l'IA ("facile").
        """
        game_root.after(1000, make_ai_move, level)

    def make_ai_move(level):
        """Fait jouer l'IA selon le niveau choisi."""
        if level == "facile":
            easy_ai_move()  # IA facile

    def easy_ai_move():
        """
        L'IA facile choisit un mouvement aléatoire parmi les cases vides.
        """
        available = available_moves()
        if available:
            move = random.choice(available)  # Choisir un mouvement aléatoire
            button_click(move[0], move[1])

    def available_moves():
        """
        Retourne la liste des mouvements disponibles (cases vides).
        
        Returns:
            list: Liste des tuples (ligne, colonne) des cases vides.
        """
        return [(r, c) for r in range(3) for c in range(3) if grid[r][c] == ' ']

    def create_buttons():
        """
        Crée les boutons de la grille Tic Tac Toe.
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

    create_buttons()  # Crée la grille de jeu
    game_root.mainloop()  # Démarre la boucle principale du jeu

# Interface de sélection de mode
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)  # Désactive le redimensionnement de la fenêtre

# Centrer la fenêtre de sélection
center_window(root, 500, 500)

mode_var = tk.StringVar()
mode_var.set("2 Joueurs")  # Mode par défaut

# Création des boutons de sélection de mode
tk.Radiobutton(root, text="2 Joueurs", variable=mode_var, value="2 Joueurs", font=("Arial", 20)).pack()
tk.Radiobutton(root, text="Jouer contre l'IA facile", variable=mode_var, value="IA Facile", font=("Arial", 20)).pack()

# Bouton pour démarrer le jeu
start_button = tk.Button(root, text="Démarrer le jeu", font=("Arial", 20), command=start_game)
start_button.pack()

root.mainloop()  # Démarre la fenêtre de sélection de mode




