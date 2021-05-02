# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:26:09 2021

@author: davide notaro
"""

#modalità scrittura (crea un nuovo file se non esiste e sovrascrive il contenuto se presente)

file_personale = open("save.txt", "w")

#modalità lettura

file_personale = open("save.txt", "r")

#aggiungere b alla fine ti permette di interagire con file non di testo
#(binary mode)

file_personale = open("save.mp3", "wb")

#per chiudere il file

file_personale.close()

#estrarre il contenuto

numero_bytes = int()
contenuto = file_personale.read()
contenuto = file_personale.read(numero_bytes) #legge solo il primo tot numero di bytes

#dopo che tutto il file è stato letto read darà un risultato vuoto

print(file_personale.readlines()) #l'output è una lista con ogni linea come elemento


#scrivere nel file

file_personale.write("yooooooo")

#la funzione restituisce il numero di byte scritti

#chiudere sempre i file nel finally oppure si usa with

with open("save.txt") as f:
    print(f.read())

