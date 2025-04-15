from requirements import *

"""
This file permit to create the figures of the system wanted to easily debug
"""


def line(n, l):
    grille = np.full((n + 2, n + 2), 1)
    for i in range(1, n + 1):
        grille[l, i] = 0
    return grille


def wall(n, column):
    grille = np.zeros((n + 2, n + 2))
    for i in range(0, n + 2):
        grille[i, column] = 1
    return grille


def outward_test():
    grille = np.zeros((50, 50))

    for i in range(50):
        for j in range(50):
            if i == j:
                grille[i][j] = 2
            if i == 50 - j:
                grille[i][j] = 1

    return grille
