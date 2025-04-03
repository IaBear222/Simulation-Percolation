from random_system_generator import *


def the_wall(syst):  # Do not work : walls are not recognized
    wall = np.sum(syst, axis=0)
    size = np.size(syst, axis=1)
    if size in wall:
        print("There is no path ")
    else:
        print("There is no straight wall")


def the_line(syst):
    line = np.sum(syst, axis=1)

    if 0 in line:
        print("There is a path")
    else:
        print("There no direct path")
