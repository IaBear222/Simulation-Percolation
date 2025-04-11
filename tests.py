from random_system_generator import *
from plot import *
from find_the_path import *
from usual_figures import *

n = 25
p = 0.5


def rdm_syst(n, p):
    syst = system(n, p)
    the_wall(syst)
    the_line(syst)
    plot_system(syst)


def line_syst(n, l):
    syst = line(n, l)
    the_wall(syst)
    the_line(syst)
    plot_system(syst)


def wall_syst(n, column):
    syst = wall(n, column)
    the_wall(syst)
    the_line(syst)
    plot_system(syst)


"""
rdm_syst(n, p)

line_syst(n, 10)

"""

wall_syst(n, 10)
