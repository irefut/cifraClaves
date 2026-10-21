# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:35:56 2023

@author: Irene

Cifra clave morse

Separadores:
    /      después de cada letra
    espacio entre palabras
    //     punto y final del mensaje

Ejemplo: "un gato salvaje" -> ..-/-./   --./.-/-/---/   .../.-/.-../...-/.-/.---/.//

Los signos (, ¿ ? " y otros) se escriben tal cual, como si fueran una
letra más. El guion (-) se escribe como = para que no se confunda con
la raya del Morse.

Faltaría agregar la clave morse en el turtle.
"""

MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "Ñ": "--.--",
    "O": "---",   "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",
    "T": "-",     "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    "-": "=",     # el guion no puede quedar como "-" porque es una raya
    "/": "\\",    # la diagonal no puede quedar como "/" porque es separador
}

# Separación entre palabras (3 espacios para que se note bien)
ESPACIO = "   "

# Las letras con tilde o diéresis se cifran igual que la letra sin tilde
SIN_TILDE = {"Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
             "Ä": "A", "Ë": "E", "Ï": "I", "Ö": "O", "Ü": "U"}


def claveMorseTexto(texto):
    print('MORSE')
    print("msj entrada: " + texto)

    mensajecifrado = ""
    for letra in texto.upper():
        letra = SIN_TILDE.get(letra, letra)

        if letra == "\n":
            # Cambio de línea: se respeta como cambio de línea
            mensajecifrado = mensajecifrado.rstrip(" ") + "\n"
        elif letra in " \t":
            # Fin de palabra: un espacio ancho. Si ya hay uno (dos espacios
            # seguidos) o estamos al inicio de una línea, no agregamos otro.
            if mensajecifrado and not mensajecifrado.endswith((" ", "\n")):
                mensajecifrado = mensajecifrado + ESPACIO
        elif letra == ".":
            # Punto: "//"
            mensajecifrado = mensajecifrado.rstrip("/") + "//"
        else:
            # Letra, número o signo: su código (o el signo tal cual) y "/"
            mensajecifrado = mensajecifrado + MORSE.get(letra, letra) + "/"

    # Final del mensaje: "//"
    mensajecifrado = mensajecifrado.rstrip(" \n")
    if mensajecifrado:
        mensajecifrado = mensajecifrado.rstrip("/") + "//"

    print('msj salida:  ' + mensajecifrado + '\n')
    return mensajecifrado

#original = input("Introduce el mensaje para cifrar: ")
#morse = claveMorseTexto("abcde fj gh ijklminñ")