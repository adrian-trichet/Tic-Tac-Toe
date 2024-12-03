import tkinter as tk

# Initialisation de la fenêtre
root = tk.Tk()
root.title("Tic Tac Toe")
root.minsize(500, 500)

# Désactiver le redimensionnement de la fenêtre
root.resizable(False, False)

# Variables pour le jeu
current_player = 'X'  # Le joueur commence avec 'X'
buttons = []
grid = [[' ' for _ in range(3)] for _ in range(3)]  # Matrice pour l'état du jeu

# Fonction pour dessiner la grille
def draw_grid():
    # Créer un Canvas pour dessiner les lignes
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.grid(row=0, column=0, columnspan=3, rowspan=3)

    # Dessiner les lignes de la grille (épaisseur des lignes = 15)
    canvas.create_line(166, 0, 166, 500, width=15)  # Ligne verticale gauche
    canvas.create_line(333, 0, 333, 500, width=15)  # Ligne verticale droite
    canvas.create_line(0, 166, 500, 166, width=15)  # Ligne horizontale du haut
    canvas.create_line(0, 333, 500, 333, width=15)  # Ligne horizontale du bas

# Fonction pour gérer les clics sur les boutons
def button_click(row, col):
    global current_player

    # Si la case est déjà remplie, ne rien faire
    if buttons[row][col]['text'] != " ":
        return

    # Mettre le symbole du joueur sur la case
    buttons[row][col].config(text=current_player)
    grid[row][col] = current_player  # Mettre à jour l'état de la grille

    # Vérifier les conditions de victoire
    victory, message = check_victory(grid)
    if victory:
        print(message)  # Afficher le message de victoire dans la console
        return

    # Changer de joueur
    current_player = 'O' if current_player == 'X' else 'X'

# Fonction pour vérifier les conditions de victoire
def check_victory(grid):
    # Vérifie les lignes
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True, f"Le joueur avec '{row[0]}' a gagné (ligne)."

    # Vérifie les colonnes
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
            return True, f"Le joueur avec '{grid[0][col]}' a gagné (colonne)."

    # Vérifie la première diagonale
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return True, f"Le joueur avec '{grid[0][0]}' a gagné (diagonale)."

    # Vérifie la deuxième diagonale
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return True, f"Le joueur avec '{grid[0][2]}' a gagné (diagonale)."

    # Si aucune condition de victoire n'est remplie
    return False, "Pas encore de victoire."

# Créer la grille et les boutons
def create_buttons():
    for row in range(3):
        button_row = []
        for col in range(3):
            # Créer un bouton pour chaque case
            button = tk.Button(root, text=" ", font=("Arial", 50), width=5, height=2,
                               command=lambda r=row, c=col: button_click(r, c))
            # Positionner les boutons sur la grille, sur les bonnes coordonnées
            button.place(x=col*166 + 10, y=row*166 + 10, width=150, height=150)
            button_row.append(button)
        buttons.append(button_row)

# Créer la grille et les boutons
draw_grid()
create_buttons()

# Lancer la fenêtre
root.mainloop()
