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
