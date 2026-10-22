# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:32:17 2023

@author: Irene

Cifrado clave Inversa:

    Escribimos abecedario al derecho y abajo al revés, quedaría algo así

    A  B  C  ... X  Y  Z
    ^  ^  ^      ^  ^  ^
    |  |  |  ... |  |  |
    V  V  V      V  V  V
    Z  Y  X  ... C  B  A
"""
from claves.sustitucion import ABECEDARIO, sustituir

# ABECEDARIO[::-1] es el abecedario al revés: "ZYXW...CBA"
TABLA = dict(zip(ABECEDARIO, ABECEDARIO[::-1]))


def claveABC(texto):
    return sustituir(texto, TABLA, "ABECEDARIO/INVERSA")
