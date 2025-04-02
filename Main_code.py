import matplotlib.pyplot as plt
import numpy as np
import random

def perco(n, p):
    grille = []
    for i in range(n):
        ligne = []  
        for j in range(n):
            if random.random() < p:
                ligne.append(0) 
            else:
                ligne.append(1) 
        grille.append(ligne) 
