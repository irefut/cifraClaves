# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:55:02 2023

@author: Irene

Cifrando clave Numérica

Numeramos desde el 1 cada letra del alfabeto, separamos cada letra por un punto(.)
y un espacio es una diagonal, y el punto(.) por una doble diagonal.
"""
def claveNumerica(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    print('NUMÉRICA')
    #print("msj: "+ mensajecifrado)
    print("msj entrada: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + "/."
        elif texto[i] == ",":
            mensajecifrado = mensajecifrado + ","
        elif texto[i] == "\"":
            mensajecifrado = mensajecifrado + "\""
        elif texto[i] == "-":
            mensajecifrado = mensajecifrado + "-"
        elif texto[i] == ".":
            mensajecifrado = mensajecifrado + "//"
        elif texto[i] == "¿":
            mensajecifrado = mensajecifrado + "¿"
        elif texto[i] == "?":
            mensajecifrado = mensajecifrado + "?//"
        elif texto[i] == "A" or texto[i] == "Á" or texto[i] == "Ä" or texto[i] == "a" or texto[i] == "á" or texto[i] == "ä":
            mensajecifrado = mensajecifrado + "1."        
        elif texto[i] == "B" or texto[i] == "b":
            mensajecifrado = mensajecifrado + "2."
        elif texto[i] == "C" or texto[i] == "c":
            mensajecifrado = mensajecifrado + "3."
        elif texto[i] == "D" or texto[i] == "d":
            mensajecifrado = mensajecifrado + "4."
        elif texto[i] == "E" or texto[i] == "É" or texto[i] == "Ë" or texto[i] == "e" or texto[i] == "é" or texto[i] == "ë":
            mensajecifrado = mensajecifrado + "5."
        elif texto[i] == "F" or texto[i] == "f":
            mensajecifrado = mensajecifrado + "6."
        elif texto[i] == "G" or texto[i] == "g":
            mensajecifrado = mensajecifrado + "7."
        elif texto[i] == "H" or texto[i] == "h":
            mensajecifrado = mensajecifrado + "8."
        elif texto[i] == "I" or texto[i] == "Í" or texto[i] == "Ï" or texto[i] == "i" or texto[i] == "í" or texto[i] == "ï":
            mensajecifrado = mensajecifrado + "9."
        elif texto[i] == "J" or texto[i] == "j":
            mensajecifrado = mensajecifrado + "10."
        elif texto[i] == "K" or texto[i] == "k":
            mensajecifrado = mensajecifrado + "11."
        elif texto[i] == "L" or texto[i] == "l":
            mensajecifrado = mensajecifrado + "12."
        elif texto[i] == "M" or texto[i] == "m":
            mensajecifrado = mensajecifrado + "13."
        elif texto[i] == "N" or texto[i] == "n":
            mensajecifrado = mensajecifrado + "14."
        elif texto[i] == "Ñ" or texto[i] == "ñ":
            mensajecifrado = mensajecifrado + "15."
        elif texto[i] == "O" or texto[i] == "Ó" or texto[i] == "Ö" or texto[i] == "o" or texto[i] == "ó" or texto[i] == "ö":
            mensajecifrado = mensajecifrado + "16."
        elif texto[i] == "P" or texto[i] == "p":
            mensajecifrado = mensajecifrado + "17."
        elif texto[i] == "Q" or texto[i] == "q":
            mensajecifrado = mensajecifrado + "18."
        elif texto[i] == "R" or texto[i] == "r":
            mensajecifrado = mensajecifrado + "19."
        elif texto[i] == "S" or texto[i] == "s":
            mensajecifrado = mensajecifrado + "20."
        elif texto[i] == "T" or texto[i] == "t":
            mensajecifrado = mensajecifrado + "21."
        elif texto[i] == "U" or texto[i] == "Ú" or texto[i] == "Ü" or texto[i] == "u" or texto[i] == "ú" or texto[i] == "ü":
            mensajecifrado = mensajecifrado + "22."
        elif texto[i] == "V" or texto[i] == "v":
            mensajecifrado = mensajecifrado + "23."
        elif texto[i] == "W" or texto[i] == "w":
            mensajecifrado = mensajecifrado + "24."
        elif texto[i] == "X" or texto[i] == "x":
            mensajecifrado = mensajecifrado + "25."
        elif texto[i] == "Y" or texto[i] == "y":
            mensajecifrado = mensajecifrado + "26."
        elif texto[i] == "Z" or texto[i] == "z":
            mensajecifrado = mensajecifrado + "27."
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('msj salida:  '+mensajecifrado+'\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
#numi = claveNumerica("L-lBD a, d. \" .ñ.ñ,ñ-ñ\"ñ")