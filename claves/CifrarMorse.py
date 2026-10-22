# -*- coding: utf-8 -*-
"""
Cifrado de clave Morse dibujada

Usa la misma convención que la clave Morse de texto (claves/morse.py):

    punto (.)  ->  punto
    raya  (-)  ->  línea
    /          ->  fin de cada letra
    espacio entre palabras
    //         ->  punto y final del mensaje

Las comillas y la coma se dibujan como en las demás claves con dibujo.
Los otros signos (¿ ? ¡ ! ...) se escriben tal cual; el guion se escribe
como = para que no se confunda con una raya.
"""
import turtle
from turtle import Turtle

from claves.morse import MORSE, SIN_TILDE


def claveMorseDibujo(Mensaje):

    turtle.title("Clave Morse")

    # Comillas curvas se dibujan como las normales
    Equivalentes = {"“": '"', "”": '"', "«": '"', "»": '"'}

    fontSize = 0.8

    # Medidas, en píxeles
    PUNTO = 9           # diámetro del punto
    RAYA = 24            # largo de la raya
    GROSOR_RAYA = 6
    SEPARACION = 6       # espacio entre los puntos y rayas de una letra
    DIAGONAL = 30        # largo de la diagonal /
    ANCHO_DIAGONAL = 23  # lo que avanza cada diagonal (15 de ancho + 8 de espacio)
    ANCHO_SIGNO = 22     # lo que ocupa un signo escrito o dibujado
    ESPACIO = 26         # espacio entre palabras
    MEDIO = 15           # altura de los puntos y rayas sobre la base de la fila
    ALTO_FILA = 50
    X_INICIO = -320
    X_LIMITE = 340       # si una palabra pasaría de aquí, va a la fila siguiente

    def InitialiseTurtle(t):
        t.speed(0)
        t.hideturtle()
        t.pensize(3)
        t.color('black')

    def PenGoto(loc, t):
        t.penup()
        t.goto(loc)
        t.pendown()

    def Flecha(locx, locy, t):
        temp = t.pensize()
        PenGoto((locx, locy), t)
        t.pensize(5*fontSize)
        t.setheading(90-45)
        t.forward(15*fontSize)
        t.setheading(-45)
        t.back(15*fontSize)
        t.setheading(-45)
        t.forward(15*fontSize)
        t.setheading(0)
        t.back(35*fontSize)
        t.pensize(temp)

    def Punto(locx, locy, t):
        # Un punto del Morse: círculo relleno
        PenGoto((locx + PUNTO/2, locy + MEDIO), t)
        t.dot(PUNTO)

    def Raya(locx, locy, t):
        # Una raya del Morse: barra gruesa (las puntas son redondas,
        # por eso empieza y termina un poco adentro)
        temp = t.pensize()
        t.pensize(GROSOR_RAYA)
        PenGoto((locx + GROSOR_RAYA/2, locy + MEDIO), t)
        t.setheading(0)
        t.forward(RAYA - GROSOR_RAYA)
        t.pensize(temp)

    def Diagonal(locx, locy, t):
        # La diagonal / que va al final de cada letra
        PenGoto((locx, locy), t)
        t.setheading(60)
        t.forward(DIAGONAL)

    def Comillas(locx, locy, t):
        temp = t.pensize()
        t.pensize(4*fontSize)
        PenGoto((locx + 7, locy + 25*fontSize), t)
        t.setheading(90-25)
        t.forward(18*fontSize)
        PenGoto((locx + 12, locy + 25*fontSize), t)
        t.setheading(90-25)
        t.forward(18*fontSize)
        t.pensize(temp)

    def Coma(locx, locy, t):
        temp = t.pensize()
        PenGoto((locx + 11, locy + 5*fontSize), t)
        t.pensize(10*fontSize)
        t.forward(0.01)
        t.setheading(90)
        t.pensize(9*fontSize)
        t.back(3)
        t.setheading(90-20)
        t.pensize(7*fontSize)
        t.back(3)
        t.setheading(90-35)
        t.pensize(5.5*fontSize)
        t.back(3)
        t.setheading(90-60)
        t.pensize(4*fontSize)
        t.back(3)
        t.pensize(temp)

    def Signo(caracter, locx, locy, t):
        # Escribe tal cual un signo que no es letra ni número (¿ ? ¡ ! ...)
        PenGoto((locx + ANCHO_SIGNO/2, locy + 1), t)
        t.penup()
        t.write(caracter, align="center", font=("Arial", 16, "bold"))

    def EsMorse(codigo):
        # True si el código son solo puntos y rayas (letras y números)
        return codigo != "" and all(s in ".-" for s in codigo)

    def AnchoLetra(i):
        # Cuánto avanza una letra, contando su diagonal del final
        codigo = MORSE.get(i, i)
        if EsMorse(codigo):
            ancho = 0
            for s in codigo:
                if s == ".":
                    ancho += PUNTO + SEPARACION
                else:
                    ancho += RAYA + SEPARACION
            return ancho + ANCHO_DIAGONAL
        return ANCHO_SIGNO + ANCHO_DIAGONAL

    def AnchoPalabra(texto, desde):
        # Cuánto mide la palabra que empieza en texto[desde]
        ancho = 0
        for i in texto[desde:]:
            i = Equivalentes.get(SIN_TILDE.get(i, i), SIN_TILDE.get(i, i))
            if i in " \t\n":
                break
            if i == ".":
                ancho += ANCHO_DIAGONAL
            else:
                ancho += AnchoLetra(i)
        return ancho

    def Letra(i, locx, locy, t):
        # Dibuja una letra (o signo) con su diagonal y devuelve dónde termina
        codigo = MORSE.get(i, i)
        if EsMorse(codigo):
            for s in codigo:
                if s == ".":
                    Punto(locx, locy, t)
                    locx += PUNTO + SEPARACION
                else:
                    Raya(locx, locy, t)
                    locx += RAYA + SEPARACION
        else:
            if i == ",":
                Coma(locx, locy, t)
            elif i == '"':
                Comillas(locx, locy, t)
            else:
                Signo(codigo, locx, locy, t)   # codigo: el guion ya viene como =
            locx += ANCHO_SIGNO
        Diagonal(locx, locy, t)
        return locx + ANCHO_DIAGONAL

    turtle.resetscreen()
    for tortuga in turtle.turtles():   # resetscreen vuelve a mostrar
        tortuga.hideturtle()           # las tortugas viejas: las escondemos
    draw = Turtle()
    InitialiseTurtle(draw)

    #Cordenada inicial
    x = X_INICIO
    y = 240

    #Indica el inicio de la clave con una flecha
    Flecha(x+25, y+5, draw)
    x += 60*fontSize

    ultimo = ""              # lo último dibujado: "letra", "punto" o nada
    inicio_palabra = True    # si la próxima letra empieza una palabra nueva

    texto = Mensaje.upper()
    for k, i in enumerate(texto):
        i = SIN_TILDE.get(i, i)
        i = Equivalentes.get(i, i)

        if i == "\n":
            # Cambio de línea en el mensaje: seguimos en la siguiente fila
            x = X_INICIO
            y -= ALTO_FILA
            inicio_palabra = True
            continue

        if i in " \t":
            # Fin de palabra: un espacio ancho (solo uno aunque haya varios)
            if not inicio_palabra:
                x += ESPACIO
            inicio_palabra = True
            continue

        if i == ".":
            # Punto: tiene que quedar "//". Si venimos de una letra ya hay
            # una diagonal y falta una; si no, se dibujan las dos.
            if ultimo == "letra":
                Diagonal(x, y, draw)
                x += ANCHO_DIAGONAL
            elif ultimo != "punto":
                Diagonal(x, y, draw)
                Diagonal(x + ANCHO_DIAGONAL, y, draw)
                x += 2 * ANCHO_DIAGONAL
            ultimo = "punto"
            continue

        if inicio_palabra:
            # Si la palabra completa no cabe en lo que queda de la fila,
            # empieza en la fila siguiente
            if x + AnchoPalabra(texto, k) > X_LIMITE and x > X_INICIO:
                x = X_INICIO
                y -= ALTO_FILA
            inicio_palabra = False
        elif x + AnchoLetra(i) > X_LIMITE:
            # Palabra más larga que una fila entera: se corta entre letras
            x = X_INICIO
            y -= ALTO_FILA

        x = Letra(i, x, y, draw)
        ultimo = "letra"

    # Final del mensaje: "//" (si ya terminó en punto, ya está)
    if ultimo == "letra":
        Diagonal(x, y, draw)
