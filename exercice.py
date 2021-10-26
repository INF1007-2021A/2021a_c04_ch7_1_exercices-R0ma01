#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

    #EXERCICE 1

from typing import Tuple
import numpy as num

def volume_elipsoide_2(axe_a=1, axe_b=1, axe_c=1, mv = 1) -> Tuple[float, float]:
    volume = (4/3)*num.pi*axe_a*axe_b*axe_c

    return (volume, (mv*volume))

    #EXERCICE 2

def trier_lettres(phrase : str) -> Tuple[dict, list]:
    dict =  {}

    for lettre in phrase :
        if not lettre in dict:
            dict[lettre] = 1
        else:
            dict[lettre]+= 1

    return dict, sorted(dict.items(), key = lambda item : item[1], reverse = True)[0][0]


## EXERCICE 3

import turtle


def recursive(chose):

    turtle.forward(10*chose)

    if chose != 0:
        turtle.left(25)
        recursive(chose-1)
        turtle.right(50)
        recursive(chose-1)
        turtle.left(25)

    turtle.backward(10*chose)


    ## EXERCICE 4

def valide(chaine):
    return bool(chaine) and all([lettre in "atgc" for lettre in chaine])

def saisie() -> Tuple[str, str]:
    chaine = None
    while not valide(chaine):
        chaine = input("veuillez entrer la chaine de charactères")
        sequence = input("veuillez entrer la séquence à verrifier")

    return chaine, sequence

def adn():
    chaine, sequence = saisie()

    pourcentage  = round(((chaine.count(sequence)) / len(chaine) * 100),2)
    return pourcentage



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    chaine = "attgcaatggtggtacatg"
    sequence = "ca"
    print("il y a "+ str(adn())+ '% de"'+ sequence+'".')


