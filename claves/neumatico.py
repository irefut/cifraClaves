# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:26:18 2023

@author: Irene

Cifrando clave neumático:

    N  E  U  M  A  T  I  C  O
    |  |  |  |  |  |  |  |  |
    V  V  V  V  V  V  V  V  V
    1  2  3  4  5  6  7  8  9
"""
from claves.sustitucion import numerada, sustituir

TABLA = numerada("NEUMATICO", "123456789")


def claveNeumatico(texto):
    return sustituir(texto, TABLA, "NEUMÁTICO")
