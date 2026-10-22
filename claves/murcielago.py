# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:36:37 2023

@author: Irene

Cifrando clave murciélago:

    M  U  R  C  I  E  L  A  G  O
    |  |  |  |  |  |  |  |  |  |
    V  V  V  V  V  V  V  V  V  V
    0  1  2  3  4  5  6  7  8  9
"""
from claves.sustitucion import numerada, sustituir

TABLA = numerada("MURCIELAGO", "0123456789")


def claveMurcielago(texto):
    return sustituir(texto, TABLA, "MURCIÉLAGO")
