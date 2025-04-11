from requirements import *


def system(n, p):
    """
    this function creates a random system of size n x n with a probability p of having a 1 in each cell.
    The system is surrounded by a wall of 1s to modelize the system borders.

    >>> input :
    n : the size of the system
    p : the probability of having a 1 in each cell wich means having matter

    <<< output:
    grille : the system created
    """
    grille = np.ones((n + 2, n + 2))
    for i in range(1, n + 1):
        for j in range(1, n + 1):

            grille[i][j] = np.random.choice([1, 0], p=[p, 1 - p])

    return grille
