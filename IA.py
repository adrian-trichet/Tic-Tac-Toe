import random

def ia_choisir_case_au_hasard(plateau):
    # Créer une liste des indices des cases vides
    cases_vides = []
    
    # Parcourir le plateau en 2D (par lignes et colonnes)
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] == ' ':  # Si la case est vide
                cases_vides.append((i, j))  # Ajouter l'indice (ligne, colonne) à la liste
    
    # Choisir un indice au hasard parmi les cases vides
    case_choisie = random.choice(cases_vides)
    
    return case_choisie

