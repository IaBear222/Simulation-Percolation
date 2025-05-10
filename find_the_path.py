from random_system_generator import *
from plot import *

"""
This file contains the functions to find a path in the system to determine if there is percolation or not.
"""


def the_wall(syst):
    """
    this function checks if there is a wall of matter in the  wich makes the system not percolate

    >>> input :
    syst : the system to check

    <<< output:
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

    >>> input :
    syst : the system to check

    <<< output:
    None : the function prints if there is a line or not
    """

    line = np.sum(syst[1:-1, 1:-1], axis=1)

    if 0 in line:
        print("There is a path")
    else:
        print("There no direct path")


from random_system_generator import *


def neighbors(syst, i, j):
    """
    this function returns the neighbors of a pixel in the system.

    >>> input :
    syst : the system to check

    i : the line of the pixel

    j : the column of the pixel

    <<< output:
    neighbors : the list of the neighbor's values of the pixel

    """
    neighbors = []

    neighbors.append(syst[i + 1, j])
    neighbors.append(syst[i - 1, j])
    neighbors.append(syst[i, j + 1])
    neighbors.append(syst[i, j - 1])

    return neighbors



def alt(syst):
    n = np.size(syst, axis=0) - 2
    syst[-1, -1] = (
        0  ## this prevent not to have free pixel at the end of the function, to make the colormap working well
    )

    for k in range(0, n + 2):
        if syst[k][1] == 0:
            syst[k][1] = 2

    for j in range(2, n + 1):
        for i in range(0, n + 1):

            neighb = neighbors(syst, i, j)

            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][j] = 2

    for j in range(0, n + 1):
        for i in range(n, 0, -1):
            neighb = neighbors(syst, i, j)

            if syst[i][j] == 0:
                if 2 in neighb:
                    syst[i][j] = 2

    if 2 in syst[:, -2]:
        print("There is a path")
        return 1, syst
    else:
        print("There is no path")
        return 0, syst
