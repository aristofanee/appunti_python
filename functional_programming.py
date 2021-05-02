# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:04:01 2021

@author: davide notaro
"""

#funcional programming

def quarta_potenza(funz, x): #le funzioni possono essere un input
    return funz(funz(x))

def seconda_potenza(x):
    return x**2

print(quarta_potenza(seconda_potenza, 3)) 

#con lambda si posso creare funzioni al momento
print(quarta_potenza(lambda x: x**2, 2)) 

#possono essere anche assegnate ad una variabile

doppio = lambda x: x*2
print(doppio(4))

#la funzione map prende una lista e una funzione come input e applica 
#la funzione ad ogni elemento

numeri = [1, 4, 7, 19]

print(list(map(lambda x: x + 3, numeri))) #attenzione l'output di map non è una lista

#filter permette di rimuovere oggetti da una lista che non rispettano una condizione

print(list(filter(lambda x: x%2 == 0, numeri))) #attenzione l'output di filter non è una lista


      
      