"""
Esta va a ser el script compartido para todas las claves de texto que cambian cada letra 
por otra cosa (otra letra, un número, etc.)

Cada clave solo tiene su TABLA: un diccionario que dice por qué se cambia cada letra. 
Las letras y signos que no están en la tabla quedan como están
"""

# Las vocales con tilde o diéresis se buscan en la tabla como la vocal sin tilde
SIN_TILDE = {"Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
             "Ä": "A", "Ë": "E", "Ï": "I", "Ö": "O", "Ü": "U"}

ABECEDARIO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def intercambio(arriba, abajo):
    """Tabla para claves de pares que se cambian entre sí (como PITA-MOBE):
    la P se cambia por M y la M por P, la I por O y la O por I, etc."""
    tabla = dict(zip(arriba, abajo))
    tabla.update(zip(abajo, arriba))
    return tabla


def numerada(palabra, numeros):
    """Tabla para claves de una palabra numerada (como MURCIELAGO-0123456789):
    cada letra de la palabra se cambia por el número de su posición."""
    return dict(zip(palabra, numeros))


def sustituir(texto, tabla, nombre):
    #Cifra el texto cambiando cada letra según la tabla
    print(nombre)
    print("msj entrada: " + texto)

    mensajecifrado = ""
    for letra in texto.upper():
        base = SIN_TILDE.get(letra, letra)    # Á -> A, Ü -> U, ...
        if base in tabla:
            mensajecifrado = mensajecifrado + tabla[base]
        else:
            mensajecifrado = mensajecifrado + letra   # no está en la tabla: queda tal cual

    print("msj salida:  " + mensajecifrado + "\n")
    return mensajecifrado
