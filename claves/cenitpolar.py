# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:19:43 2023

@author: Irene

Cifrando clave Cenit Polar:

    C  E  N  I  T
    ^  ^  ^  ^  ^
    |  |  |  |  |
    V  V  V  V  V
    P  O  L  A  R
"""
from claves.sustitucion import intercambio, sustituir

TABLA = intercambio("CENIT", "POLAR")


def claveCenitPolar(texto):
    return sustituir(texto, TABLA, "CENIT POLAR")
