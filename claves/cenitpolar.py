# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:19:43 2023

@author: Irene

Cifrando Cenit Polar
"""
def claveCenitPolar(texto):
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
        elif texto[i] == "C" or texto[i] == "c":
            mensajecifrado = mensajecifrado + "P"        
        elif texto[i] == "E" or texto[i] == "É" or texto[i] == "Ë" or texto[i] == "e" or texto[i] == "é" or texto[i] == "ë":
            mensajecifrado = mensajecifrado + "O"
        elif texto[i] == "N" or texto[i] == "n":
            mensajecifrado = mensajecifrado + "L"
        elif texto[i] == "I" or texto[i] == "Í" or texto[i] == "Ï" or texto[i] == "i" or texto[i] == "í" or texto[i] == "ï":
            mensajecifrado = mensajecifrado + "A"
        elif texto[i] == "T" or texto[i] == "t":
            mensajecifrado = mensajecifrado + "R"
        elif texto[i] == "P" or texto[i] == "p":
            mensajecifrado = mensajecifrado + "C"
        elif texto[i] == "O" or texto[i] == "Ó" or texto[i] == "Ö" or texto[i] == "o" or texto[i] == "ó" or texto[i] == "ö":
            mensajecifrado = mensajecifrado + "E"
        elif texto[i] == "L" or texto[i] == "l":
            mensajecifrado = mensajecifrado + "N"
        elif texto[i] == "A" or texto[i] == "Á" or texto[i] == "Ä" or texto[i] == "a" or texto[i] == "á" or texto[i] == "ä":
            mensajecifrado = mensajecifrado + "I"
        elif texto[i] == "R" or texto[i] == "r":
            mensajecifrado = mensajecifrado + "T"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('msj salida:  '+mensajecifrado+'\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
#cenit = claveCenitPolar(original)
