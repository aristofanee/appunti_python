# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:58:53 2021

@author: davno
"""

lista = ["latte", "uova", "pasta"]

if "pasta" in lista:
    print("bona la pasta")
    
lista.append("carne")

if "carne" in lista:
    print("bona la carne")
    
lista.insert(1, "sugo")

if "sugo" in lista:
    print("bono il sugo")
    
print(lista)

print(lista.index("carne"))

print(lista.count("latte"))

lista.remove("latte")

lista.reverse()

print(lista)


print(lista[0:2])

numeri = list(range(10))

print(numeri[2:6])
print(numeri[:7])
print(numeri[0:7])
print(numeri[0:7:2]) #lo step è l'ultimo numero, possono essere negativi e contare dalla fine della lista


cubi = [num**3 for num in range(20)]
print(cubi)

cubi_2 = [num**3 for num in range(20) if num**3 > 20]
print(cubi_2)


lista_test = [3, 5, 3, 2, 10, 2]
if all(m > 1 for m in lista_test):
    print("maggiori di uno")
    
if any(m==2 for m in lista_test):
    print("c'è un due")
    
    
for v in enumerate(lista_test):
    print(v)
    
