# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:12:22 2023

@author: Irene

Cifrando clave abuelito:

    A  B  U  E  L  I  T  O
    |  |  |  |  |  |  |  |
    V  V  V  V  V  V  V  V
    1  2  3  4  5  6  7  8
"""
from claves.sustitucion import numerada, sustituir

TABLA = numerada("ABUELITO", "12345678")


def claveAbuelito(texto):
    return sustituir(texto, TABLA, "ABUELITO")
