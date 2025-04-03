from random_system_generator import *


def plot_system(syst):

    n = np.size(syst, axis=0)

    visu = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if syst[i][j] == 1:
                visu[i][j] = 1
            elif syst[i][j] == 0:
                visu[i][j] = 0
            elif syst[i][j] == 2:
                visu[i][j] = 0.5

    plt.imshow(visu, cmap="Blues")
    plt.title("grille de percolation ")
    plt.show()


"""
Observation : à p= 0 et p= 1 il affiche tt en noir !!
"""
