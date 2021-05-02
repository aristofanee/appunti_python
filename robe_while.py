# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:43:53 2021

@author: davno
"""
numeri = list()

while True:
    n = input("inserisci un numero: ")
    
    if n == 'stop':
        break
    
    numeri.append(float(n))
    

print(numeri)

dispari = list()    

while True:
    b = input("lista dei numeri dispari: ")
    
    if b == 'stop':
        break
    
    if int(b)%2 == 0:
        continue
    else:
        dispari.append(float(b))
    
print(dispari)