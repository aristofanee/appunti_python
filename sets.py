# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:40:44 2021

@author: davide notaro
"""

#sets

parole = {"ciao", "gatto", "tubo"} #sono simili alle liste
numeri = {0, 2, 3, 6, 8}

for i in parole: #notare che l'ordine non corrisponde
    print(i)

print("ciao" in parole)

#le differenze principali sono:
    #non possono essere indicizzate (non hanno ordine)
    #non possono contere duplicati
    
parole.add("cane")
parole.remove("gatto")

for i in parole:
    print(i)
    
#ci sono poi gli operatori classici degli insiemi

numeri_2 = {2, 7, 3, 4, 5}

print(numeri|numeri_2) #unione
print(numeri&numeri_2) #intersezione
print(numeri-numeri_2) #differenza
print(numeri^numeri_2) #simmetria (aut)

