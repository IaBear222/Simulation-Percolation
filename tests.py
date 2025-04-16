from random_system_generator import *
from plot import *
from find_the_path import *
from usual_figures import *

n = 100
p = 0.5


def rdm_syst(n, p):
    syst = system(n, p)
    the_wall(syst)
    the_line(syst)
    syst = outward(syst)
    _, syst = backward(syst)

    plot_system(syst, p)


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


def test_color(nb):
    syst = np.full((n, n), nb)
    plot_system(syst)


rdm_syst(n, p)

"""
l_syst(n, 10)

wall_syst(n, 10)
outward_syst()
test_color(0)


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
