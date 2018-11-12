import random
import numpy as np
from random import randint # para gerar os nums aleatorios

def criaVetor(L, H, tam):
    vec = []
    for i in range(tam): # vamos fazer isto tam (N) vezes
        vec.append(randint(L, H)) # gerar numero aleatorio entre L e H, e colocar na nossa lista
    return vec

Npop = 4
Maq = 2
i = 0

m = list(range(1,Maq+1))
j = list(range(1,Npop+1))

while i <= Npop:
    N = random.sample(range(1,5), 4)
    print(N)

    M = criaVetor(1,2,4)
    print(M)

    P = random.sample(range(1,5),4)
    print(P,'\n')

    pred_list = []

    for h in M:
        for j in N:
            if N[j] == M[0]:
                pred_list=pred_list
            else:
                pred_list.append(N[j])
                print(pred_list)




    i = i+1

