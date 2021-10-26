#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(0, "C:\\Users\\trila\\OneDrive\\Bureau\\Bacc Polytechnique\\Session 1 (A21)\\"
                   "Intro. à la programmation python (INF1007)\\2021a-c01-ch6-1-exercices-Tristanlach")
from exercice_6 import frequence
import turtle
from turtle import*

# TODO: Définissez vos fonction ici
def ellipsoide(a = 1, b = 2, c = 3, masse_volumique = 1):

    volume = (4/3) * math.pi * a * b * c
    masse = masse_volumique * volume

    return volume, masse

def draw_tree():
    setheading(90)
    color("green")

    #rappeler fonction recursive
    draw_branch(70, 7, 35)

    done()

def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len -10, pen_size -1, angle -5)
        left(2 * angle)
        draw_branch(branch_len -10, pen_size -1, angle -5)
        right(angle)
        backward(branch_len)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(ellipsoide(2, 3, 4, 2 ))
    print((lambda sentence : sorted(frequence(sentence).items(), key = lambda x: x[1])[-1][0])("bonjour, je suis une phraseee."))
    draw_tree()