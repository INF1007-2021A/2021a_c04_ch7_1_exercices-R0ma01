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

#fun stufff
def choisir_une_couleur(n):
    if n ==1 :
        turtle.color("green")
    elif n == 2:
        turtle.color("red")
    elif n== 3 :
        turtle.color("purple")
    elif n== 4 :
        turtle.color("blue")
    elif n== 5:
        turtle.color("yellow")
    else:
        turtle.color("orange")


#référence au petit prince

def dessine_moi_un_arbre(iteration:int, angle:int, grandeur: int):
    choisir_une_couleur(iteration)
    turtle.forward(grandeur*iteration)

    if iteration != 0:
        turtle.pensize(iteration)
        turtle.left(angle)

        dessine_moi_un_arbre((iteration-1), angle, grandeur)
        turtle.right(angle*2)
        dessine_moi_un_arbre((iteration-1), angle, grandeur)
        turtle.left(angle)

    turtle.pensize(iteration)
    turtle.backward(grandeur*iteration)







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
    turtle.left(90)
    turtle.speed(3)
    dessine_moi_un_arbre(5, 25, 10)

