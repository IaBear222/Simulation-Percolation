from libraries import *
from plot import *
from find_a_path import *


n = 50
p = 0.5


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


def rdm_syst(n, p):
    syst = system(n, p)
    the_wall(syst)
    the_line(syst)
    _, syst = alt(syst)
    plot_system(syst, p)


rdm_syst(n, p)


def run_boucle(n, p, repet):
    """ """
    compteur = 0

    for _ in range(repet):
        syst = system(n, p)
        path, syst = alt(syst)
        if path == 1:
            compteur += 1

    Taux = 100 * compteur / repet

    print(f"\nNombre de chemins trouvés : {compteur} sur {repet}")
    print(f"Taux de percolation : {Taux:.2f}%")


run_boucle(n, p, 5)
