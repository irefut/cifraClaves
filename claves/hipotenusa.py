# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:46:22 2023

@author: Irene

Cifrando clave hipotenusa:

    H  I  P  O  T  E  N  U  S  A
    |  |  |  |  |  |  |  |  |  |
    V  V  V  V  V  V  V  V  V  V
    1  2  3  4  5  6  7  8  9  0
"""
from claves.sustitucion import numerada, sustituir

TABLA = numerada("HIPOTENUSA", "1234567890")


def claveHipotenusa(texto):
    return sustituir(texto, TABLA, "HIPOTENUSA")
