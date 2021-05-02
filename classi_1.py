# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:50:34 2021

@author: davno
"""

#classi

class cane:
    def __init__(self, colore, taglia): #questo è il modo di definire una classe
        self.colore = colore #init è il "metodo" principale
        self.taglia = taglia
        
    def saluta(self): #il primo parametro è sempre self
        print("bau, sono " + self.colore)
        
        
gino = cane("nero", "media")

print(gino.taglia)

gino.saluta()

class Piante:
    def __init__(self, altezza, colore):
        self.altezza = altezza
        self.colore = colore
    

class Albero(Piante):
    def forza(self):
       print("sono un alberop")
        

acero = Albero(18, "verde")
acero.forza()


class A:
    def lolli(self):
        print(1)
        
class B(A):
    def lol(self):
        print(2)
        super().lolli() #super chiama i metodi della superclasse

B().lol()
    
        
