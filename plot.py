from libraries import *


cm = Colormap("seaborn:tab20b")  # colormap for the plot


def plot_system(syst, p):
    """
    Fonction to plot the system with the different values of the pixels depending on their value

    inputs :
        syst : the system to plot
        p : the probability of getting a particule in each place of space

    outputs :
        the plot of the system
    """

    n = np.size(syst, axis=0)

    visu = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if syst[i][j] == 1:  # check if the pixel is a particule
                visu[i][j] = 0
            elif syst[i][j] == 0:  # check if the pixel is an empty space
                visu[i][j] = 255
            elif syst[i][j] == 2:  # check if the pixel is a path
                visu[i][j] = 50

    # Generating the plot of the system with the different values of the pixels
    plt.imshow(visu, cmap="gist_earth")
    plt.title(
        f"grille de percolation pour {n-2}*{n-2} particules (p={p})",
        fontname="Times New Roman",
        fontstyle="italic",
    )
    plt.show()
