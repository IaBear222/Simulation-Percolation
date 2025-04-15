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
    neighbors = []

    neighbors.append((i + 1, j))
    neighbors.append((i - 1, j))
    neighbors.append((i, j + 1))
    neighbors.append((i, j - 1))

    return neighbors


def outward(syst):
    n = np.size(syst, axis=0) - 2

    for i in range(2, n + 1):
        for j in range(1, n + 1):
            neighb = neighbors(syst, i, j)
            if syst[i][j] == 0:
                if (
                    1 and (0 or 2) in neighb
                ):  # /!\ And et Or priorité ??? ==> option : 2 boucles if
                    syst[i][j] = 2

    plot_system(syst)


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
