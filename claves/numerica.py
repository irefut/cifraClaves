# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:55:02 2023

@author: Irene

Cifrando clave Numérica

Numeramos desde el 1 cada letra del alfabeto, separamos cada letra por un punto(.)
y un espacio es una diagonal, y el punto(.) por una doble diagonal.
"""
from claves.sustitucion import ABECEDARIO, sustituir

# A -> "1.", B -> "2.", ..., Z -> "27."
TABLA = {letra: str(numero) + "." for numero, letra in enumerate(ABECEDARIO, start=1)}
TABLA[" "] = "/."
TABLA["."] = "//"
TABLA["?"] = "?//"


def claveNumerica(texto):
    return sustituir(texto, TABLA, "NUMÉRICA")
