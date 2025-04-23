from random_system_generator import *
from plot import *

"""
This file contains the functions to find a path in the system to determine if there is percolation or not.
"""


def the_wall(syst):
    """
    this function checks if there is a wall of matter in the  wich makes the system not percolate

    >>> input :
    syst : the system to check

    <<< output:
    None : the function prints if there is a wall or not

    """
    wall = np.sum(syst[1:-1, 1:-1], axis=0)
    size = np.size(syst, axis=0) - 2
    if size in wall:
        print("There is no path ")
    else:
        print("There is no straight wall")


def the_line(syst):
    """
    this function checks if there is a line of matter in the  which makes the system percolate

    >>> input :
    syst : the system to check

    <<< output:
    None : the function prints if there is a line or not
    """

    line = np.sum(syst[1:-1, 1:-1], axis=1)

    if 0 in line:
        print("There is a path")
    else:
        print("There no direct path")


from random_system_generator import *


def neighbors(syst, i, j):
    """
    this function returns the neighbors of a pixel in the system.

    >>> input :
    syst : the system to check

    i : the line of the pixel

    j : the column of the pixel

    <<< output:
    neighbors : the list of the neighbor's values of the pixel

    """
    neighbors = []
    """
    neighbors.append(syst[i + 1, j])
    neighbors.append(syst[i - 1, j])
    neighbors.append(syst[i, j + 1])
    neighbors.append(syst[i, j - 1])
    """
    # au lieu d'enregistrer la valeur des cases voisines on va simplement enregistrer leur position
    neighbors.append((i + 1, j))
    neighbors.append((i , j + 1))
    neighbors.append((i - 1, j))
    neighbors.append((i , j -1 ))
    
    return neighbors




def alt(syst):
    n = np.size(syst, axis=0) - 2
    syst[-1, -1] = (
        0  ## this prevent not to have free pixel at the end of the function, to make the colormap working well
    )

    for k in range(0, n + 2):
        if syst[k][1] == 0:
            syst[k][1] = 2
    """
    for j in range(2, n + 1):
        for i in range(0, n + 1):

            neighb = neighbors(syst, i, j)

            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][j] = 2
    
    for j in range(n, 0, -1):
        for i in range(0, n + 1):
            neighb = neighbors(syst, i, j)
            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][j] = 2
    
    for j in range(0, n + 1):
        for i in range(0, n + 1):
            neighb = neighbors(syst, i, j)

            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][j] = 2
    
    for j in range(0, n + 1):
        for i in range(n, 0, -1):
            neighb = neighbors(syst, i, j)
            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][j] = 2
    """
    stack = [] #création d'une liste vide qui va nous permettre de stocker toutes les positions voisines qui seront vide
    
    #précédemment on a changé la valeur de toutes les cases vides de la premieres colonne par 2, donc avec ce bloc on va stocker toutes ces valeurs pour pouvoir regarder leurs voisins dans la boucle d'après
    for i in range(n):
        if syst[i, 1] == 2:
            stack.append((i, 1))

    #La boucle permet dans un premier temps de regarder tous les voisins libre de la premiere colonne( à partir d'une case visité) puis par la suite continuer le calcul pour les voisins des voisins ect..
    while stack:
        i, j = stack.pop(0)  #retire le premier élément de la liste c'est à dire l'élément qu'on regarde actuellement (la boucle while commence par le 1er élement)
        
        
        for x, y in neighbors(syst, i, j): #retourne une liste de coordonnées (x, y) des voisins du pixel situé à la position (i, j)
            if syst[x, y] == 0: # vérifie si les cases à la position (x,y) ont une valeur de 0
                syst[x, y] = 2 #si c'est le cas ils seront considérés comme visité
                stack.append((x, y)) #donc ces valeurs seront ajoutées dans la liste pour pouvoir regarder leurs voisins à eux
    """
    Cette boucle parcourt tous les voisins du pixel actuel (i, j). Pour chaque voisin qui n'a pas encore été marqué, elle le marque
    avec la valeur 2 et l'ajoute à la file d'attente. Ce qui permet propager les cases visitées à travers le syst de manière continue, 
    en explorant tous les chemins possibles simultanément dans les quatre directions
    """
    if 2 in syst[:, -2]:
        print("There is a path")
        return 1, syst
    else:
        print("There is no path")
        return 0, syst
    
