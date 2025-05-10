from random_system_generator import *
from plot import *
from find_the_path import *


n = 10
p = 0.25


def rdm_syst(n, p):
    syst = system(n, p)
    the_wall(syst)
    the_line(syst)
    syst = outward(syst)
    _, syst = backward(syst)

    plot_system(syst, p)


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
