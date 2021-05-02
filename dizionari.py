# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:37:29 2021

@author: davno
"""

#dizionari


anni = {"Marco": 23, "Gianni": 12, "Zero": 14}

print(anni["Marco"])

colori = {
    "rosso": [255, 0, 0],
    "verde": [0, 255, 0],
    "blu": [0 , 0, 255]
    }

print(colori["blu"])


quadrati = {1: 1, 2: 4, 3: "errore", 4 :16}

print(quadrati[3])

quadrati[8] = 64
quadrati[3] = 9

print(quadrati)



print(1 in quadrati)
print(3 in quadrati)
print(16 in quadrati)


cose = {"blallo": 9, 
        9: 1, 4: "pube",
        True: False,
        None: "True"
        }

print(cose.get("blallo")) 
print(cose.get(9))
print(cose.get(45, "nope")) #se l'elemento non è presente
print(cose.get(9, 0))


