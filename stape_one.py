from random_system_generator import *


def neighbors(syst, i, j):
    neighbors = []

    neighbors.append((i + 1, j))
    neighbors.append((i - 1, j))
    neighbors.append((i, j + 1))
    neighbors.append((i, j - 1))

    return neighbors


def aller(syst):
    n = np.size(syst, axis=0) - 2
    for i in range(2, n + 1):
        for j in range(1, n + 1):
            neighbors = neighbors(syst, i, j)
            if syst[i][j] == 0:
                if (
                    1 and (0 or 2) in neighbors
                ):  # /!\ And et Or priorité ??? ==> option : 2 boucles if
                    syst[i][j] = 2
