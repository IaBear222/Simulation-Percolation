from libraries import *
from plot import *
from find_a_path import *

n = 500
p = 0.75
repet= 10

def rdm_syst(n, p):
    """
    Function to create a random system of size n with a probability p and verify if there is a direct path or if there is a wall
    """
    syst = system(n, p) #generate the system
    the_wall(syst) #check if there is a wall
    the_line(syst)#check if there is a direct line

    plot_system(syst, p)


def run_boucle(n, p, repet): 
    """
     Function to create a random system of size n with a probability p and generate a path in the system and if there is a path, then it will print the number of paths found and the percolation rate
    """
    compteur = 0  #initialization of the counter

    for _ in range(repet): #to repeat the process a certain number of times
        syst = system(n, p) #generate the system
        path, syst = alt(syst) #generate the path in the system
        if path == 1: #check if there is a path
            compteur += 1 #increment the counter

    Taux = 100 * compteur / repet #calculate the percolation rate

    print(f"\nNombre de chemins trouvés : {compteur} sur {repet}")
    print(f"Taux de percolation : {Taux:.2f}%")


run_boucle(n, p, repet)
