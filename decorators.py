# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:06:03 2021

@author: davide notaro
"""

#decorators
#i decoratori sono funzioni che modificano altre funzioni aggiungendo roba

def stampa_testo():
    print("yoo")
         
         
def decor(funz):
    def abbellisci():
        print("=======")
        funz() #attenzione qua, non bisogna mettere "stampa_testo"
        print("=======")
    return abbellisci
    
    
    
stampa_testo = decor(stampa_testo) #la funzione viene "aggiornata"

stampa_testo()

@decor #la sostituzione precedente può essere fatta in questa maniera molto più compatta
def II_stampa_testo():
    print("yeahhh boii")
    
    
II_stampa_testo()