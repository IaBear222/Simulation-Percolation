"""
This file is used to run the simulation of percolation,
It generates a random system of size n with a probability p of gatting a particule in each place of space .
Then it verifies if there is or not percolation

inputs :
    n : int : size of the system
    p : float : probability of getting a particule in each place of space
    repet : int : number of times to repeat the process

outputs :
    the system may be plotted with the particules and limits of the system using rdm_syst function
    the percolation rate and the number of paths found this kind of system using run_boucle function

"""

from libraries import *
from plot import *
from find_a_path import *

n = 50
p = 0.75
repet = 5


def system(n, p):
    """
    this function creates a random system of size n x n with a probability p of having a 1 in each cell.
    The system is surrounded by a wall of 1s to modelize the system borders.

    input :
        n : the size of the system
        p : the probability of having a 1 in each cell wich means having matter

    output:
        grille : the system created
    """
    # create the system sized n x n with frame of matter ( to facilitate computes later)
    grille = np.ones((n + 2, n + 2))
    # generate empty spaces
    for i in range(1, n + 1):
        for j in range(1, n + 1):

            grille[i][j] = np.random.choice([1, 0], p=[p, 1 - p])

    return grille


def rdm_syst(n, p):
    """
    This function for a random generated system  if there is or not percolation
    Then plot the system wyth some of the ways borrowable

        inputs :
            n : int : size of the system
            p : float : probability of getting a particule in each place of space

        outputs :
            the plot of the system
    """

    syst = system(n, p)  # generate the system
    the_wall(syst)  # check if there is a wall
    the_line(syst)  # check if there is a direct line
    _, syst = perco_finder(syst)  # find the path in the system

    plot_system(syst, p)


def run_boucle(n, p, repet):
    """
    This function creates a repet number of random systems of size n with a probability p of each particule to appear
    in or der to verify how many times there is or not percolation

    inputs :
        n : int : size of the system
        p : float : probability of getting a particule in each place of space
        repet : int : number of times to repeat the process

    outputs :
        the percolation rate and the number of paths found in the system
    """

    compteur = 0  # it will count the number of percolations observed

    for _ in range(repet):
        syst = system(n, p)  # generate the system
        path, syst = perco_finder(syst)  # look for percolation in the system

        if path == 1:  # check if there is percolation
            compteur += 1

    Taux = 100 * compteur / repet  # calculate the percolation rate

    print(f"\nNombre de chemins trouvés : {compteur} sur {repet}")
    print(f"Taux de percolation : {Taux:.2f}%")


run_boucle(n, p, repet)
