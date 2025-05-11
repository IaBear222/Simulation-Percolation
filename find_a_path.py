from plot import *

"""
This file contains the functions to find a path in the system to determine if there is percolation or not.
"""


def the_wall(syst):
    """
    this function checks if there is a wall of matter in the  wich makes the system not percolate

    input :
    syst : the system to check

    output:
    None : the function prints if there is a wall or not

    """
    wall = np.sum(syst[1:-1, 1:-1], axis=0)
    size = np.size(syst, axis=0) - 2
    if size in wall:
        print("There is no path ")
    else:
        print("There is no straight wall")


def the_line(syst):
    """
    this function checks if there is a line of matter in the  which makes the system percolate

    input :
        syst : the system to check

    output:
        None : the function prints if there is a line or not
    """

    line = np.sum(syst[1:-1, 1:-1], axis=1)

    if 0 in line:
        return "ther is a path "
    else:
        return "there is no evident path "


def neighbors(syst, i, j):
    """
    This function index neighbors' values of a pixel in the system.

    input :
        syst : the system to check

        i : the line of the pixel

        j : the column of the pixel

    output:
        neighbors : the list of the neighbors' values of the pixel

    """

    neighbors = []

    neighbors.append(syst[i + 1, j])  # lower neighbor
    neighbors.append(syst[i - 1, j])  # upper neighbor
    neighbors.append(syst[i, j + 1])  # right neighbor
    neighbors.append(syst[i, j - 1])  # left neighbor

    return neighbors


def perco_finder(syst):
    """
    This function finds a path in the system to determine if there is percolation or not.
    It uses the neighbors function to check if there is a path in the system.

    input :
        syst : the system to check

    output:
        path : 1 if there is a path, 0 if there is no path
        syst : the system with the path
    """

    ### preventing not to have free pixel at the end of the function, to make the colormap working well ###
    n = np.size(syst, axis=0) - 2
    syst[-1, -1] = 0

    ###initialize the first line ###
    for k in range(0, n + 2):
        if syst[k][1] == 0:
            syst[k][1] = 2

    ### computing first in increasing direction ###
    for j in range(2, n + 1):
        for i in range(0, n + 1):

            neighb = neighbors(syst, i, j)  # get the neighbors' values of the pixel

            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][
                        j
                    ] = 2  # a possible path unit should be preceding by anotrher one

    ### computing then in decreasing direction to prevent mistakes due to the order of operations ###

    for j in range(0, n + 1):
        for i in range(n, 0, -1):
            neighb = neighbors(syst, i, j)

            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][j] = 2

    ### checking if the last column is directly connected to the first column ###
    if 2 in syst[:, -2]:
        return 1, syst

    else:
        return 0, syst
