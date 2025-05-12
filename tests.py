from random_system_generator import *
from plot import *
from find_the_path import *
from usual_figures import *

n = 10
p = 0.25


def rdm_syst(n, p):
    syst = system(n, p)
    the_wall(syst)
    the_line(syst)
    syst = outward(syst)
    _, syst = backward(syst)

    plot_system(syst, p)


def l_syst(n, l):
    syst = line(n, l)

    _, syst = alt(syst)

    plot_system(syst, p)


def wall_syst(n, column):
    syst = wall(n, column)
    the_wall(syst)
    the_line(syst)
    plot_system(syst,p)


def outward_syst():
    syst = outward_test()
    the_wall(syst)
    the_line(syst)
    syst = outward(syst)
    plot_system(syst,p)


def test_color(nb):
    """ """
    syst = np.full((n, n), nb)
    plot_system(syst,p)


def alt_syst(syst, n, p):
    _, syst = alt(syst)
    plot_system(syst, p)

def run_boucle(n, p, repet):
    compteur = 0

    for _ in range(repet):
        syst = system(n, p)
        path, syst = alt(syst)  
        if path == 1:
            compteur += 1
        plot_system(syst, p)

    
    Taux = 100 * compteur / repet   


    print(f"\nNombre de chemins trouvés : {compteur} sur {repet}")
    print(f"Taux de percolation : {Taux:.2f}%")

run_boucle(n,p,5)

alt_syst(anti_line(n, 5), n, p)

"""


rdm_syst(n, p)

wall_syst(n, 10)
outward_syst()
test_color(0)
l_syst(n, 7)  

tab = np.array(
    [
        [0, 1, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0],
    ]
)

s = np.sum(tab[1:-1, 1:-1], axis=1)
print(s)
"""
