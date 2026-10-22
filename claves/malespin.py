# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:45:32 2023

@author: Irene

Cifrado clave Malespín:

    P  I  T  A
    ^  ^  ^  ^
    |  |  |  |
    V  V  V  V
    M  O  B  E
"""
from claves.sustitucion import intercambio, sustituir

TABLA = intercambio("PITA", "MOBE")


def claveMalespin(texto):
    return sustituir(texto, TABLA, "MALESPÍN")
