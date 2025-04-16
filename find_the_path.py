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


def outward(syst):
    """
    this function is the first step to find if there is a path in any kind of system.

    It will change the vaue of each free pixel next to matter and another free pixel to 2 in purpuse to find a pth following "walls" of matter.

    >>> input :
    syst : the system to check

    <<< output:
    another system : the system with the new values
    """
    n = np.size(syst, axis=0) - 2

    for i in range(2, n + 1):
        for j in range(1, n + 1):
            neighb = neighbors(syst, i, j)
            if syst[i][j] == 0:
                if 1 in neighb and (
                    0 in neighb or 2 in neighb
                ):  # /!\ And et Or priorité ??? ==> option : 2 boucles if
                    syst[i][j] = 2

    return syst


def backward(syst):
    n = np.size(syst, axis=0) - 2
    for k in range(0, n):
        if syst[n - 1][k] == 0 or 2:
            syst[n - 1][k] = 3

    for i in range(n, 0):
        for j in range(-1, 0):
            neighb = neighbors(syst, i, j)
            if 3 and (2 or 3) in neighb:  ## comment signifier le double 3
                syst[i][j] = 3

    plot_system(syst)
