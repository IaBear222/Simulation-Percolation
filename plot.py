from random_system_generator import *


def plot_system(n, p):

    syst = system(n, p)

    visu = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if syst[i][j] == 1:
                visu[i][j] = 1
            elif syst[i][j] == 0:
                visu[i][j] = 0
            elif syst[i][j] == 2:
                visu[i][j] = 0.5

    plt.imshow(visu, cmap="grey")
    plt.title("grille de percolation ")
    plt.show()
