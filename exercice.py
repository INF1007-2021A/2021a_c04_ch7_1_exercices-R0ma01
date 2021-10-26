#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

    #EXERCICE 1

from typing import Tuple
import numpy as num

def volume_elipsoide_2(a, b, c) -> Tuple:

    return (4/3)*num.pi*a*b*c

    #EXERCICE 2

#En reprenant le 5e exercice du chapitre 6 sur les fréquences de lettres dans une phrase,
#écrivez un programme qui trie les lettres à partir du dictionnaire et qui retourne la lettre avec la fréquence la plus haute,
#en utilisant une fonction lambda.



## EXERCICE 3

import turtle
turtle.color("green")

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

def valide(chaine, sequence):
    return (
        True if chaine != None and sequence != None else
        False
    )


def adn(adn, sequence):
    pourcentage  = round(((adn.count(sequence)) / len(adn) * 100),2)
    return (
        pourcentage if valide(adn, sequence) else
        False
    )

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    chaine = "attgcaatggtggtacatg"
    sequence = "ca"
    print(adn(chaine, sequence))


