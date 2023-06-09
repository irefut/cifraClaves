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
def claveHipotenusa(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    #print("msj: "+ mensajecifrado)
    print('HIPOTENUSA')
    print("msj entrada: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + " "
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "."
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "-"
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?"
        elif texto[i] == "H" or texto[i] == "h":
            mensajecifrado = mensajecifrado + "1"        
        elif texto[i] == "I" or texto[i] == "Í" or texto[i] == "Ï" or texto[i] == "i" or texto[i] == "í" or texto[i] == "ï":
            mensajecifrado = mensajecifrado + "2"
        elif texto[i] == "P" or texto[i] == "p":
            mensajecifrado = mensajecifrado + "3"
        elif texto[i] == "O" or texto[i] == "Ó" or texto[i] == "Ö" or texto[i] == "o" or texto[i] == "ó" or texto[i] == "ö":
            mensajecifrado = mensajecifrado + "4"
        elif texto[i] == "T" or texto[i] == "t":
            mensajecifrado = mensajecifrado + "5"
        elif texto[i] == "E" or texto[i] == "É" or texto[i] == "Ë" or texto[i] == "e" or texto[i] == "é" or texto[i] == "ë":
            mensajecifrado = mensajecifrado + "6"
        elif texto[i] == "N" or texto[i] == "n":
            mensajecifrado = mensajecifrado + "7"
        elif texto[i] == "U" or texto[i] == "Ú" or texto[i] == "Ü" or texto[i] == "u" or texto[i] == "ú" or texto[i] == "ü":
            mensajecifrado = mensajecifrado + "8"
        elif texto[i] == "S" or texto[i] == "s":
            mensajecifrado = mensajecifrado + "9"
        elif texto[i] == "A" or texto[i] == "Á" or texto[i] == "Ä" or texto[i] == "a" or texto[i] == "á" or texto[i] == "ä":
            mensajecifrado = mensajecifrado + "0"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('msj salida:  '+mensajecifrado+'\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
#hipo = claveHipotenusa(original)
