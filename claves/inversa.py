# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:32:17 2023

@author: Irene
"""
def claveABC(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    print('ABECEDARIO/INVERSA')
    print("msj entrada: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + " "
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "-"
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "."
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?"
        elif texto[i] == "A" or texto[i] == "Á" or texto[i] == "Ä" or texto[i] == "a" or texto[i] == "á" or texto[i] == "ä":
            mensajecifrado = mensajecifrado + "Z"        
        elif texto[i] == "B" or texto[i] == "b":
            mensajecifrado = mensajecifrado + "Y"
        elif texto[i] == "C" or texto[i] == "c":
            mensajecifrado = mensajecifrado + "X"
        elif texto[i] == "D" or texto[i] == "d":
            mensajecifrado = mensajecifrado + "W"
        elif texto[i] == "E" or texto[i] == "É" or texto[i] == "Ë" or texto[i] == "e" or texto[i] == "é" or texto[i] == "ë":
            mensajecifrado = mensajecifrado + "V"
        elif texto[i] == "F" or texto[i] == "f":
            mensajecifrado = mensajecifrado + "U"
        elif texto[i] == "G" or texto[i] == "g":
            mensajecifrado = mensajecifrado + "T"
        elif texto[i] == "H" or texto[i] == "h":
            mensajecifrado = mensajecifrado + "S"
        elif texto[i] == "I" or texto[i] == "Í" or texto[i] == "Ï" or texto[i] == "i" or texto[i] == "í" or texto[i] == "ï":
            mensajecifrado = mensajecifrado + "R"
        elif texto[i] == "J" or texto[i] == "j":
            mensajecifrado = mensajecifrado + "Q"
        elif texto[i] == "K" or texto[i] == "k":
            mensajecifrado = mensajecifrado + "P"
        elif texto[i] == "L" or texto[i] == "l":
            mensajecifrado = mensajecifrado + "O"
        elif texto[i] == "M" or texto[i] == "m":
            mensajecifrado = mensajecifrado + "Ñ"
        elif texto[i] == "N" or texto[i] == "n":
            mensajecifrado = mensajecifrado + "N"
        elif texto[i] == "Ñ" or texto[i] == "ñ":
            mensajecifrado = mensajecifrado + "M"
        elif texto[i] == "O" or texto[i] == "Ó" or texto[i] == "Ö" or texto[i] == "o" or texto[i] == "ó" or texto[i] == "ö":
            mensajecifrado = mensajecifrado + "L"
        elif texto[i] == "P" or texto[i] == "p":
            mensajecifrado = mensajecifrado + "K"
        elif texto[i] == "Q" or texto[i] == "q":
            mensajecifrado = mensajecifrado + "J"
        elif texto[i] == "R" or texto[i] == "r":
            mensajecifrado = mensajecifrado + "I"
        elif texto[i] == "S" or texto[i] == "s":
            mensajecifrado = mensajecifrado + "H"
        elif texto[i] == "T" or texto[i] == "t":
            mensajecifrado = mensajecifrado + "G"
        elif texto[i] == "U" or texto[i] == "Ú" or texto[i] == "Ü" or texto[i] == "u" or texto[i] == "ú" or texto[i] == "ü":
            mensajecifrado = mensajecifrado + "F"
        elif texto[i] == "V" or texto[i] == "v":
            mensajecifrado = mensajecifrado + "E"
        elif texto[i] == "W" or texto[i] == "w":
            mensajecifrado = mensajecifrado + "D"
        elif texto[i] == "X" or texto[i] == "x":
            mensajecifrado = mensajecifrado + "C"
        elif texto[i] == "Y" or texto[i] == "y":
            mensajecifrado = mensajecifrado + "B"
        elif texto[i] == "Z" or texto[i] == "z":
            mensajecifrado = mensajecifrado + "A"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('msj salida:  '+mensajecifrado+'\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
#inversa = claveABC(original)