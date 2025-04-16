from random_system_generator import *
from plot import *
from find_the_path import *
from usual_figures import *

n = 250
p = 0.78


def rdm_syst(n, p):
    syst = system(n, p)
    the_wall(syst)
    the_line(syst)
    syst = outward(syst)
    plot_system(syst)


def l_syst(n, l):
    syst = line(n, l)
    the_wall(syst)
    the_line(syst)
    plot_system(syst)


def wall_syst(n, column):
    syst = wall(n, column)
    the_wall(syst)
    the_line(syst)
    plot_system(syst)


def outward_syst():
    syst = outward_test()
    the_wall(syst)
    the_line(syst)
    syst = outward(syst)
    plot_system(syst)


rdm_syst(n, p)
"""
l_syst(n, 10)
wall_syst(n, 10)

outward_syst()
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
