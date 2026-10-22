# -*- coding: utf-8 -*-
"""
Dibuja una clave con turtle en su propio proceso, separado de la ventana
de Qt. Así cada programa de ventanas (Qt y turtle/Tk) tiene su propio
ciclo de eventos y no se pelean.

La ventana principal (GUI/mainwindow.py) lo ejecuta así:
    python -m claves.dibujar gato
y le manda el texto a codificar por la entrada estándar (stdin).
"""
import base64
import turtle
import tkinter

from claves.CifrarGato import claveGato
from claves.CifrarChina import claveChina
from claves.CifarSieteCruces import claveSieteCruces
from claves.CifrarMusical import claveMusical
from claves.CifrarBailarin import claveBailarin

CLAVES = {
    "gato": claveGato,
    "china": claveChina,
    "sietecruces": claveSieteCruces,
    "musical": claveMusical,
    "bailarin": claveBailarin,
}

# Tamaño de la ventanita, en píxeles.
ANCHO = 710
ALTO = 620

def dibujar_desde_texto64(nombre, texto64):
    texto = base64.urlsafe_b64decode(texto64).decode("utf-8")
    try:
        turtle.setup(width=ANCHO, height=ALTO)
        CLAVES[nombre](texto)
        turtle.mainloop()   # mantiene la ventanita abierta hasta que la cierren
    except (turtle.Terminator, tkinter.TclError):
        # Cerraron la ventanita antes de que terminara de dibujar:
        # no es un error, simplemente dejamos de dibujar
        pass