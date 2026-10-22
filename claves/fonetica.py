# -*- coding: utf-8 -*-
"""
Cifra clave Fonética (alfabeto fonético: Alfa, Bravo, Charlie, Delta...)

Cada letra se cambia por su palabra del alfabeto fonético.

Separadores:
    espacio  entre letras
    /        entre palabras
    //       punto

La Ñ, que no está en el alfabeto fonético internacional, le pusimos Ñoño.
Los números se dicen en español (Uno, Dos, ...). Los signos (, ¿ ? " y
otros) se escriben tal cual, como si fueran una letra más.
"""

FONETICA = {
    "A": "Alfa",     "B": "Bravo",    "C": "Charlie",  "D": "Delta",
    "E": "Echo",     "F": "Foxtrot",  "G": "Golf",     "H": "Hotel",
    "I": "India",    "J": "Juliett",  "K": "Kilo",     "L": "Lima",
    "M": "Mike",     "N": "November", "Ñ": "Ñoño",     "O": "Oscar",
    "P": "Papa",     "Q": "Quebec",   "R": "Romeo",    "S": "Sierra",
    "T": "Tango",    "U": "Uniform",  "V": "Victor",   "W": "Whiskey",
    "X": "X-ray",    "Y": "Yankee",   "Z": "Zulu",
    "1": "Uno",      "2": "Dos",      "3": "Tres",     "4": "Cuatro",
    "5": "Cinco",    "6": "Seis",     "7": "Siete",    "8": "Ocho",
    "9": "Nueve",    "0": "Cero",
}

# Las letras con tilde o diéresis se cifran igual que la letra sin tilde
SIN_TILDE = {"Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
             "Ä": "A", "Ë": "E", "Ï": "I", "Ö": "O", "Ü": "U"}


def cifrarLinea(linea):
    # Vamos juntando los pedazos de la línea: palabras del alfabeto,
    # signos y separadores ("/" o "//"). Al final se unen con espacios.
    pedazos = []
    for letra in linea:
        letra = SIN_TILDE.get(letra, letra)

        if letra in " \t":
            # Fin de palabra: "/" (solo uno aunque haya varios espacios,
            # y ninguno si ya hay un separador o la línea está empezando)
            if pedazos and pedazos[-1] not in ("/", "//"):
                pedazos.append("/")
        elif letra == ".":
            # Punto: "//" (reemplaza al "/" si venía uno antes)
            if pedazos and pedazos[-1] == "/":
                pedazos.pop()
            if not pedazos or pedazos[-1] != "//":
                pedazos.append("//")
        else:
            # Letra, número o signo: su palabra (o el signo tal cual)
            pedazos.append(FONETICA.get(letra, letra))

    # Un "/" suelto al final de la línea sobra
    if pedazos and pedazos[-1] == "/":
        pedazos.pop()
    return " ".join(pedazos)


def claveFonetica(texto):
    print('FONÉTICA')
    print("msj entrada: " + texto)

    # Cada línea del mensaje se cifra por aparte (se respetan los cambios de línea)
    lineas = [cifrarLinea(linea) for linea in texto.upper().split("\n")]
    mensajecifrado = "\n".join(lineas)

    print('msj salida:  ' + mensajecifrado + '\n')
    return mensajecifrado
