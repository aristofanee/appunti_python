# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:41:52 2021

@author: davide notaro
"""

#itertools

import itertools


for i in itertools.count(3): #conta infinitamente
    print(i)
    
    if(i>9):
        break

lista = [1,2,3,4,5,6]

for numero in itertools.cycle(lista): #cicla infinitamente
    print(numero)
    
    break
    
    
for n in itertools.repeat(2): #ripete infinitamente
    print(n)
    
    break
    

lista = [3,6,2,5,3,4,7,4,3]
print(list(itertools.takewhile(lambda x: x<5, lista))) #prende item da una lista
#finche una certa condizione rimane vera

lista_2 = [3,7,1,3]

print(list(itertools.chain(lista,lista_2))) #unisce iterabili

print(list(itertools.accumulate(lista))) #somma progressiva dei valori di un iterabile

lettere_1 = ("A","B","C")
lettere_2 = ("E","F","G")

print(list(itertools.product(lettere_1, lettere_2))) #prodotto cartesiano tra due iterabili
print(list(itertools.permutations(lettere_1))) #tutte le permutazioni possibili