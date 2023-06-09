# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:31:29 2023

@author: Irene

Cifrando clave PARELINOFU:
    
    P  R  L  N  F
    ^  ^  ^  ^  ^  
    |  |  |  |  |  
    V  V  V  V  V  
    A  E  I  O  U

"""
def claveParelinofu(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    #print("msj: "+ mensajecifrado)
    print('PARELINOFU')
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
        elif texto[i] == "P" or texto[i] == "p":
            mensajecifrado = mensajecifrado + "A"        
        elif texto[i] == "A" or texto[i] == "Á" or texto[i] == "Ä" or texto[i] == "a" or texto[i] == "á" or texto[i] == "ä":
            mensajecifrado = mensajecifrado + "P"
        elif texto[i] == "R" or texto[i] == "r":
            mensajecifrado = mensajecifrado + "E"
        elif texto[i] == "E" or texto[i] == "É" or texto[i] == "Ë" or texto[i] == "e" or texto[i] == "é" or texto[i] == "ë":
            mensajecifrado = mensajecifrado + "R"
        elif texto[i] == "L" or texto[i] == "l":
            mensajecifrado = mensajecifrado + "I"
        elif texto[i] == "I" or texto[i] == "Í" or texto[i] == "Ï" or texto[i] == "i" or texto[i] == "í" or texto[i] == "ï":
            mensajecifrado = mensajecifrado + "L"
        elif texto[i] == "N" or texto[i] == "n":
            mensajecifrado = mensajecifrado + "O"
        elif texto[i] == "O" or texto[i] == "Ó" or texto[i] == "Ö" or texto[i] == "o" or texto[i] == "ó" or texto[i] == "ö":
            mensajecifrado = mensajecifrado + "N"
        elif texto[i] == "F" or texto[i] == "f":
            mensajecifrado = mensajecifrado + "U"
        elif texto[i] == "U" or texto[i] == "Ú" or texto[i] == "Ü" or texto[i] == "u" or texto[i] == "ú" or texto[i] == "ü":
            mensajecifrado = mensajecifrado + "F"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('msj salida:  '+mensajecifrado+'\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
#pare = claveParelinofu(original)

