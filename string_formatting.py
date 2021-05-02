# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:17:27 2021

@author: davide notaro
"""

#string formatting

numeri = [1, 2, 3]

errore = "i numeri permessi sono: {1} {0} {2}". format(numeri[0], numeri[1], numeri[2])

print(errore)


print(", ".join(["carne", "pesce", "mucca"]))

#join trasforma una lista in una stringa e aggiunge un certo separatore

print("pollo, cacca, spiscio".split(", "))

#split è l'opposto di join e trasforma le stringe in liste

print("yooo bovino".replace("bovino", "mucca"))

#replace sostituisce

print("bella frate zio".startswith("bella"))
print("bella frate zio".endswith("zio"))

#endswith e startswith danno valori booleani e si spiegano abbastanza da soli

print("no vabbe ziooo".upper())
print("GIURO NON STO URLANDO".lower())

#allcaps o nulla in caps