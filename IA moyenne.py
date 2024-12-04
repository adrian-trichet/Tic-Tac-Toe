import tkinter as tk
import random

# Initialisation de la fenêtre
root = tk.Tk()
root.title("Tic Tac Toe")
root.minsize(500, 500)
root.resizable(False, False)

# Variables globales
current_player = 'X'  # Le joueur commence avec 'X'
grid = [[' ' for _ in range(3)] for _ in range(3)]  # Grille du jeu
buttons = []  # Liste pour stocker les boutons
message_label = tk.Label(root, text="", font=("Arial", 20))
message_label.grid(row=3, column=0, columnspan=3)

# Fonction pour vérifier les conditions de victoire
def check_victory(grid):
    # Vérifie les lignes
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True, f"Le joueur avec '{row[0]}' a gagné !"

    # Vérifie les colonnes
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
            return True, f"Le joueur avec '{grid[0][col]}' a gagné !"

    # Vérifie les diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return True, f"Le joueur avec '{grid[0][0]}' a gagné !"
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return True, f"Le joueur avec '{grid[0][2]}' a gagné !"

    # Si aucune condition de victoire
    return False, ""

# Désactiver les boutons
def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")

# Fonction pour gérer les clics du joueur
def button_click(row, col):
    global current_player

    if buttons[row][col]['text'] != " ":
        return

    # Joueur joue
    buttons[row][col].config(text=current_player)
    grid[row][col] = current_player

    # Vérifier victoire ou égalité
    victory, message = check_victory(grid)
    if victory:
        message_label.config(text=message)
        disable_buttons()
        return

    if all(cell != ' ' for row in grid for cell in row):
        message_label.config(text="Égalité !")
        disable_buttons()
        return

    # Tour de l'IA
    current_player = 'O'
    ai_row, ai_col = ai_move(grid)
    buttons[ai_row][ai_col].config(text=current_player)
    grid[ai_row][ai_col] = current_player

    # Vérifier victoire après le coup de l'IA
    victory, message = check_victory(grid)
    if victory:
        message_label.config(text=message)
        disable_buttons()
        return

    if all(cell != ' ' for row in grid for cell in row):
        message_label.config(text="Égalité !")
        disable_buttons()
        return

    # Revenir au joueur humain
    current_player = 'X'

# Fonction de l'IA
def ai_move(grid):
    # Vérifier si l'IA peut gagner
    for row in range(3):
        for col in range(3):
            if grid[row][col] == ' ':
                grid[row][col] = 'O'
                if check_victory(grid)[0]:
                    grid[row][col] = ' '
                    return row, col
                grid[row][col] = ' '

    # Vérifier si l'IA doit bloquer le joueur
    for row in range(3):
        for col in range(3):
            if grid[row][col] == ' ':
                grid[row][col] = 'X'
                if check_victory(grid)[0]:
                    grid[row][col] = ' '
                    return row, col
                grid[row][col] = ' '

    # Privilégier le centre
    if grid[1][1] == ' ':
        return 1, 1

    # Jouer dans un coin si possible
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for row, col in corners:
        if grid[row][col] == ' ':
            return row, col

    # Jouer aléatoirement
    empty_cells = [(row, col) for row in range(3) for col in range(3) if grid[row][col] == ' ']
    return random.choice(empty_cells)

# Créer les boutons
def create_buttons():
    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(root, text=" ", font=("Arial", 50), width=5, height=2,
                               command=lambda r=row, c=col: button_click(r, c))
            button.grid(row=row, column=col, padx=5, pady=5)
            button_row.append(button)
        buttons.append(button_row)

# Lancer le jeu
create_buttons()
root.mainloop()
