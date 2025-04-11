from requirements import *

"""
This file permit to create the figures of the system wanted to easily debug
"""


def line(n, line):
    grille = np.full((n, n), 1)
    for i in range(0, n):
        grille[line, i] = 0
    return grille


def wall(n, column):
    grille = np.zeros((n, n))
    for i in range(0, n):
        grille[i, column] = 1
    return grille
