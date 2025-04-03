import matplotlib.pyplot as plt
import numpy as np
import random


def system(n, p):
    grille = np.zeros((n, n))
    for i in range(n):
        for j in range(n):

            grille[i][j] = np.random.choice([1, 0], p=[p, 1 - p])

    return grille
