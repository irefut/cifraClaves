# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:35:56 2023

@author: Irene

Cifra clave morse

Faltaría agregar la clave morse en el turtle.
"""
def claveMorseTexto(texto):
    longitud=len(texto) #Calculamos la longitud del texto para recorrerlo
    mensajecifrado = ""
    #print(longitud)
    print('MORSE')
    print("msj entrada: "+texto)
    for i in range (0,longitud): #Bucle para recorrer el texto
        if texto[i] == " ":
            mensajecifrado = mensajecifrado + "/"
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
            mensajecifrado = mensajecifrado + "?"
        elif texto[i] == "A" or texto[i] == "Á" or texto[i] == "Ä" or texto[i] == "a" or texto[i] == "á" or texto[i] == "ä":
            mensajecifrado = mensajecifrado + ".-/"        
        elif texto[i] == "B" or texto[i] == "b":
            mensajecifrado = mensajecifrado + "-.../"
        elif texto[i] == "C" or texto[i] == "c":
            mensajecifrado = mensajecifrado + "-.-./"
        elif texto[i] == "D" or texto[i] == "d":
            mensajecifrado = mensajecifrado + "-../"
        elif texto[i] == "E" or texto[i] == "É" or texto[i] == "Ë" or texto[i] == "e" or texto[i] == "é" or texto[i] == "ë":
            mensajecifrado = mensajecifrado + "./"
        elif texto[i] == "F" or texto[i] == "f":
            mensajecifrado = mensajecifrado + "..-./"
        elif texto[i] == "G" or texto[i] == "g":
            mensajecifrado = mensajecifrado + "--./"
        elif texto[i] == "H" or texto[i] == "h":
            mensajecifrado = mensajecifrado + "..../"
        elif texto[i] == "I" or texto[i] == "Í" or texto[i] == "Ï" or texto[i] == "i" or texto[i] == "í" or texto[i] == "ï":
            mensajecifrado = mensajecifrado + "../"
        elif texto[i] == "J" or texto[i] == "j":
            mensajecifrado = mensajecifrado + ".---/"
        elif texto[i] == "K" or texto[i] == "k":
            mensajecifrado = mensajecifrado + "-.-/"
        elif texto[i] == "L" or texto[i] == "l":
            mensajecifrado = mensajecifrado + ".-../"
        elif texto[i] == "M" or texto[i] == "m":
            mensajecifrado = mensajecifrado + "--/"
        elif texto[i] == "N" or texto[i] == "n":
            mensajecifrado = mensajecifrado + "-./"
        elif texto[i] == "Ñ" or texto[i] == "ñ":
            mensajecifrado = mensajecifrado + "--.--/"
        elif texto[i] == "O" or texto[i] == "Ó" or texto[i] == "Ö" or texto[i] == "o" or texto[i] == "ó" or texto[i] == "ö":
            mensajecifrado = mensajecifrado + "---/"
        elif texto[i] == "P" or texto[i] == "p":
            mensajecifrado = mensajecifrado + ".--./"
        elif texto[i] == "Q" or texto[i] == "q":
            mensajecifrado = mensajecifrado + "--.-/"
        elif texto[i] == "R" or texto[i] == "r":
            mensajecifrado = mensajecifrado + ".-./"
        elif texto[i] == "S" or texto[i] == "s":
            mensajecifrado = mensajecifrado + ".../"
        elif texto[i] == "T" or texto[i] == "t":
            mensajecifrado = mensajecifrado + "-/"
        elif texto[i] == "U" or texto[i] == "Ú" or texto[i] == "Ü" or texto[i] == "u" or texto[i] == "ú" or texto[i] == "ü":
            mensajecifrado = mensajecifrado + "..-/"
        elif texto[i] == "V" or texto[i] == "v":
            mensajecifrado = mensajecifrado + "...-/"
        elif texto[i] == "W" or texto[i] == "w":
            mensajecifrado = mensajecifrado + ".--/"
        elif texto[i] == "X" or texto[i] == "x":
            mensajecifrado = mensajecifrado + "-..-/"
        elif texto[i] == "Y" or texto[i] == "y":
            mensajecifrado = mensajecifrado + "-.--/"
        elif texto[i] == "Z" or texto[i] == "z":
            mensajecifrado = mensajecifrado + "--../"
        elif texto[i] == "1":
            mensajecifrado = mensajecifrado + ".----/"
        elif texto[i] == "2":
            mensajecifrado = mensajecifrado + "..---/"
        elif texto[i] == "3":
            mensajecifrado = mensajecifrado + "...--/"
        elif texto[i] == "4":
            mensajecifrado = mensajecifrado + "....-/"
        elif texto[i] == "5":
            mensajecifrado = mensajecifrado + "...../"
        elif texto[i] == "6":
            mensajecifrado = mensajecifrado + "-..../"
        elif texto[i] == "7":
            mensajecifrado = mensajecifrado + "--.../"
        elif texto[i] == "8":
            mensajecifrado = mensajecifrado + "---../"
        elif texto[i] == "9":
            mensajecifrado = mensajecifrado + "----./"
        elif texto[i] == "0":
            mensajecifrado = mensajecifrado + "-----/"
        else:
            mensajecifrado = mensajecifrado + texto[i]
    print('msj salida:  '+mensajecifrado+'\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
morse = claveMorseTexto("abcde fj gh ijklminñ")