from random_system_generator import *
from plot import *
from find_the_path import *

n = 5
p = 0.5
syst = system(n, p)
the_wall(syst)
the_line(syst)

plot_system(n, p)
