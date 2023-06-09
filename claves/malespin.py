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
def claveMalespin(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    print('MALESPÍN')
    print("msj entrada: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + " "
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "."
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "-"
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?"
        elif texto[i] == "P" or texto[i] == "p":
            mensajecifrado = mensajecifrado + "M"        
        elif texto[i] == "I" or texto[i] == "Í" or texto[i] == "Ï" or texto[i] == "i" or texto[i] == "í" or texto[i] == "ï":
            mensajecifrado = mensajecifrado + "O"
        elif texto[i] == "T" or texto[i] == "t":
            mensajecifrado = mensajecifrado + "B"
        elif texto[i] == "A" or texto[i] == "Á" or texto[i] == "Ä" or texto[i] == "a" or texto[i] == "á" or texto[i] == "ä":
            mensajecifrado = mensajecifrado + "E"
        elif texto[i] == "M" or texto[i] == "m":
            mensajecifrado = mensajecifrado + "P"
        elif texto[i] == "O" or texto[i] == "Ó" or texto[i] == "Ö" or texto[i] == "o" or texto[i] == "ó" or texto[i] == "ö":
            mensajecifrado = mensajecifrado + "I"
        elif texto[i] == "B" or texto[i] == "b":
            mensajecifrado = mensajecifrado + "T"
        elif texto[i] == "E" or texto[i] == "É" or texto[i] == "Ë" or texto[i] == "e" or texto[i] == "é" or texto[i] == "ë":
            mensajecifrado = mensajecifrado + "A"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('msj salida:  '+mensajecifrado+'\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
#malespin = claveMalespin(original)