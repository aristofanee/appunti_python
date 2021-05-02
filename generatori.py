# -*- coding: utf-8 -*-
"""
Created on Sun May  2 13:46:55 2021

@author: davide notaro
"""

#generatori


def capodanno():
    i = 10
    
    while i>0:
        yield i #yield trasforma la funzione in un generatore
        i = i-1 
        

for k in capodanno():
    print(k)
    
    
print(list(capodanno())) #i generatori (finiti) possnon essere trasformati in liste
