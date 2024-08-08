
import numpy as np
import math



# Modello markoviano


A=np.array([[8/17, 9/28, 8/11],\
            [0, 9/28, 2/11],\
            [9/17, 5/14, 1/11]])



# Condizione iniziale random

x0=np.random.rand(3,1)

# Normalizzo il vettore e lo rendo stocastico

x0=x0/np.sum(x0)

# Vedo l'andamento per un numero di passi arbitrario

npassi=200

for i in range(npassi):
    x0=A@x0
    
print( x0)