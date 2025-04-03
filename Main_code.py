import matplotlib.pyplot as plt
import numpy as np
import random

def perco(n, p):
    grille = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                grille[i][j]=0
            else:
                grille[i][j]=1
    return grille 

def visu(grille):

    visu = np.zeros((n, n))


    for i in range(n):
        for j in range(n):
            if grille[i][j] == 1:
                visu[i][j] = 1 
            elif grille[i][j] == 0:
                visu[i][j] = 0  
            elif grille[i][j] == 2:
                visu[i][j] = 0.5

    
    plt.imshow(visual_grid, cmap='gray')
    plt.colorbar(label='0 = libre, 1 = fermé, 2 = visitée')
    plt.title("grille de percolation ")
    plt.show()

