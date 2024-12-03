def init_grid():
    # Retourne une liste de 3 sous-listes, chacune contenant 3 espaces vides
    # Cela représente une grille 3x3 initialisée pour le jeu
    # "_" est une convention qui permet de ne pas utiliser une variable dans une boucle for
    # dans ce cas elle permet juste de répéter l'action 3 fois
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_grid(grid):
    # Parcourt chaque ligne de la grille
    for row in grid:
        # Affiche la ligne actuelle en joignant les cases avec une barre verticale (|)
        print('|'.join(row))
        
        # Affiche une ligne de séparation entre les lignes de la grille
        # Cette ligne de séparation a une longueur de 5 (trois colonnes et deux séparateurs)
        print('-' * 5)

<<<<<<< HEAD:main.py

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

grid = init_grid()
grid[0][0] = "x"
grid[0][1] = "x"
grid[1][2] = "x"
grid[2][1] = "x"
display_grid(grid)
print(check_victory(grid))


=======
def afficher_message( joueur,resultat):
    if resultat == "victoire":
        print(f"Le joueur {joueur} a gagné !")
    elif resultat=="défaite":
      print(f"lejoueur {joueur} a perdu")
    elif resultat == "match_nul":
        print("C'est un match nul !")
    else:
        print(f"un bug")
>>>>>>> 8fafb10fb049d1ea19d80df44e6ebe8aadead804:mess_system.py
