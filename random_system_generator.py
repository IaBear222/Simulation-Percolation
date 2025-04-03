import matplotlib.pyplot as plt
import numpy as np
import random


def system(n, p):
    grille = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                grille[i][j] = 0
            else:
                grille[i][j] = 1

    return grille
