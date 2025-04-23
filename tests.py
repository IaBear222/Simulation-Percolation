from random_system_generator import *
from plot import *
from find_the_path import *
from usual_figures import *

n = 300
p = 0.3



syst = system(n, p)
the_wall(syst)
the_line(syst)
alt(syst)

plot_system(syst,p)
"""
alt_syst(n, p)

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
