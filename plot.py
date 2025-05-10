from libraries import *


cm = Colormap("seaborn:tab20b")  # colormap for the plot


def plot_system(syst, p):
    """
    Fonction to plot the system with the different values of the pixels
    
    """
    n = np.size(syst, axis=0)

    visu = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if syst[i][j] == 1:  #value of the wall
                visu[i][j] = 0        
            elif syst[i][j] == 0:   #value of the empty space
                visu[i][j] = 255    
            elif syst[i][j] == 2:   #value of the path
                visu[i][j] = 50     


    plt.imshow(visu, cmap="gist_earth")  #image of the system with the different values of the pixels
    plt.title(
        f"grille de percolation pour {n-2} particules (p={p})", 
        fontname="Times New Roman",
        fontstyle="italic",
    )
    plt.show() 
