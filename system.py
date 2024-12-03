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

def afficher_message( joueur,resultat):
    if resultat == "victoire":
        print(f"Le joueur {joueur} a gagné !")
    elif resultat=="défaite":
      print(f"lejoueur {joueur} a perdu")
    elif resultat == "match_nul":
        print("C'est un match nul !")
    else:
        print(f"un bug")



 


    
    
    

grid = init_grid()

display_grid(grid)
 
