from random_system_generator import *

cm = Colormap("seaborn:tab20b")


def plot_system(syst, p):

    n = np.size(syst, axis=0)

    visu = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if syst[i][j] == 1:
                visu[i][j] = 0
            elif syst[i][j] == 0:
                visu[i][j] = 255
            elif syst[i][j] == 2:
                visu[i][j] = 50

            elif syst[i][j] == 3:
                visu[i][j] = 120

    plt.imshow(visu, cmap="gist_earth")
    plt.title(
        f"grille de percolation pour {n-2} particules (p={p})",
        fontname="Times New Roman",
        fontstyle="italic",
    )
    plt.show()


"""

"""
