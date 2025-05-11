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

n = 500
p = 0.75
repet = 10


def rdm_syst(n, p):
    """
    This function creates a random system of size n with a probability p of each particule to appear
    Then verify if there is or not percolation while plotting the system wyth some of the ways followable

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

    compteur = 0  # initialization of the counter

    for _ in range(repet):  # to repeat the process a certain number of times
        syst = system(n, p)  # generate the system
        path, syst = perco_finder(syst)  # generate the path in the system
        if path == 1:  # check if there is a path
            compteur += 1  # increment the counter

    Taux = 100 * compteur / repet  # calculate the percolation rate

    print(f"\nNombre de chemins trouvés : {compteur} sur {repet}")
    print(f"Taux de percolation : {Taux:.2f}%")


run_boucle(n, p, repet)
