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

# Fonction pour dessiner la grille
def draw_grid():
    # Créer un Canvas pour dessiner les lignes
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.grid(row=0, column=0, columnspan=3, rowspan=3)

    # Dessiner les lignes de la grille (épaisseur des lignes = 5)
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

    # Changer de joueur
    current_player = 'O' if current_player == 'X' else 'X'

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
