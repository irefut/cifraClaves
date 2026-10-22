# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:31:29 2023

@author: Irene

Cifrando clave PARELINOFU:

    P  R  L  N  F
    ^  ^  ^  ^  ^
    |  |  |  |  |
    V  V  V  V  V
    A  E  I  O  U
"""
from claves.sustitucion import intercambio, sustituir

TABLA = intercambio("PRLNF", "AEIOU")


def claveParelinofu(texto):
    return sustituir(texto, TABLA, "PARELINOFU")
