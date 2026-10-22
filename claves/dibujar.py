# -*- coding: utf-8 -*-
"""
Dibuja una clave con turtle en su propio proceso, separado de la ventana
de Qt. Así cada programa de ventanas (Qt y turtle/Tk) tiene su propio
ciclo de eventos y no se pelean.

La ventana principal (GUI/mainwindow.py) lo ejecuta así:
    python main.py --dibujar gato <texto> <archivo>
(o CodificadorScout.exe --dibujar gato <texto> <archivo>, en el ejecutable)
El texto va en base64 para que tildes, comillas y cambios de línea
viajen sin problemas.

Al terminar de dibujar, guarda en <archivo> la lista de todo lo que se
dibujó (líneas, rellenos y textos). La ventana principal la usa para
armar la imagen cuando se toca el botón Copiar (ver GUI/recorte.py).
"""
import base64
import json
import os
import tkinter
import tkinter.font
import turtle

from claves.CifrarGato import claveGato
from claves.CifrarChina import claveChina
from claves.CifrarSieteCruces import claveSieteCruces
from claves.CifrarMusical import claveMusical
from claves.CifrarBailarin import claveBailarin
from claves.CifrarMorse import claveMorseDibujo

CLAVES = {
    "gato": claveGato,
    "china": claveChina,
    "sietecruces": claveSieteCruces,
    "musical": claveMusical,
    "bailarin": claveBailarin,
    "morse": claveMorseDibujo,
}

# Tamaño de la ventanita, en píxeles.
ANCHO = 710
ALTO = 620

# Para calcular cuánto espacio puede necesitar un mensaje largo
# (se calcula con la clave que más espacio usa: pocas letras por fila
# y filas altas, para que siempre alcance)
LETRAS_POR_FILA = 11
ALTO_FILA = 80
Y_INICIO = 300       # los dibujos empiezan arriba, cerca de y = 300
Y_ARRIBA = 300       # lo más alto que se muestra (deja margen sobre el dibujo)
MARGEN = 40          # espacio en blanco debajo del dibujo

# Hasta dónde llega el dibujo hacia abajo (se usa al mover la ventana)
estado = {"alto_abajo": 0}


def ajustar_lienzo(alto_abajo, ir_arriba=True):
    """Deja el lienzo desde arriba del dibujo hasta y = -alto_abajo.
    Si no cabe en la ventanita, muestra la barra para bajar."""
    estado["alto_abajo"] = alto_abajo
    lienzo = turtle.getcanvas()   # el marco de turtle, con las barras
    canvas = lienzo._canvas       # el lienzo de dibujo que está adentro

    lienzo.hscroll.grid_forget()  # la barra horizontal nunca hace falta
    alto_visible = canvas.winfo_height()
    abajo = alto_abajo + MARGEN
    if Y_ARRIBA + abajo > alto_visible:
        # No cabe: mostramos la barra para bajar
        lienzo.vscroll.grid(padx=1, in_=lienzo, pady=1, row=0, column=1, sticky="news")
    else:
        # Cabe: sin barra, y el lienzo del alto justo de la ventanita
        lienzo.vscroll.grid_forget()
        abajo = alto_visible - Y_ARRIBA
    canvas.update_idletasks()     # que la barra termine de aparecer o desaparecer

    # A diferencia de turtle, el lienzo empieza justo arriba del dibujo
    # (así no queda espacio en blanco arriba) y queda centrado a lo ancho
    ancho_visible = canvas.winfo_width()
    canvas.config(scrollregion=(-ancho_visible // 2, -Y_ARRIBA,
                                ancho_visible // 2, abajo))
    if ir_arriba:
        canvas.yview_moveto(0)    # mostrar el inicio del dibujo


def al_cambiar_ventana(evento):
    # Si mueven o cambian el tamaño de la ventanita, volvemos a acomodar
    # el lienzo, pero sin mover lo que la persona está viendo
    ajustar_lienzo(estado["alto_abajo"], ir_arriba=False)


def bajar_con_rueda(evento):
    # La rueda del mouse mueve el dibujo hacia arriba o hacia abajo
    turtle.getcanvas().yview_scroll(int(-evento.delta / 120), "units")


def guardar_trazos(canvas, ruta):
    """Guarda en el archivo 'ruta' todo lo que quedó dibujado en el lienzo:
    líneas, figuras rellenas y textos, con su posición, grosor y color."""

    def color(nombre_color):
        # Pasa un color de Tk ("black", "grey", ...) a formato "#rrggbb"
        if not nombre_color:
            return None
        r, g, b = canvas.winfo_rgb(nombre_color)   # cada uno va de 0 a 65535
        return "#%02x%02x%02x" % (r // 256, g // 256, b // 256)

    # Cuántos píxeles mide un punto de letra en esta pantalla
    pixeles_por_punto = float(canvas.tk.call("tk", "scaling"))

    trazos = []
    for item in canvas.find_all():   # en orden: primero lo que quedó más abajo
        tipo = canvas.type(item)
        puntos = canvas.coords(item)
        if tipo == "line":
            linea = color(canvas.itemcget(item, "fill"))
            if linea and puntos:
                trazos.append({"tipo": "linea", "puntos": puntos,
                               "ancho": float(canvas.itemcget(item, "width")),
                               "color": linea})
        elif tipo == "polygon":
            relleno = color(canvas.itemcget(item, "fill"))
            borde = color(canvas.itemcget(item, "outline"))
            # Las tortugas escondidas son polígonos sin color: esas no van
            if (relleno or borde) and any(puntos):
                trazos.append({"tipo": "poligono", "puntos": puntos,
                               "ancho": float(canvas.itemcget(item, "width")),
                               "relleno": relleno, "borde": borde})
        elif tipo == "text":
            fuente = tkinter.font.Font(root=canvas, font=canvas.itemcget(item, "font")).actual()
            tamano = fuente["size"]   # positivo: en puntos; negativo: en píxeles
            pixeles = round(tamano * pixeles_por_punto) if tamano > 0 else -tamano
            trazos.append({"tipo": "texto", "texto": canvas.itemcget(item, "text"),
                           "caja": list(canvas.bbox(item)),
                           "familia": fuente["family"], "pixeles": pixeles,
                           "negrita": fuente["weight"] == "bold",
                           "color": color(canvas.itemcget(item, "fill")) or "#000000"})

    # Se escribe primero en otro archivo y luego se renombra, para que la
    # ventana principal nunca lea un archivo a medio escribir
    temporal = ruta + ".tmp"
    with open(temporal, "w", encoding="utf-8") as archivo:
        json.dump(trazos, archivo)
    os.replace(temporal, ruta)


def dibujar_desde_texto64(nombre, texto64, ruta_trazos=None):
    texto = base64.urlsafe_b64decode(texto64).decode("utf-8")
    try:
        turtle.setup(width=ANCHO, height=ALTO)
        lienzo = turtle.getcanvas()
        lienzo.update()   # que la ventanita termine de aparecer
        # Cambiamos cómo turtle acomoda el lienzo y agregamos la rueda del mouse
        lienzo._rootwindow.bind("<Configure>", al_cambiar_ventana)
        lienzo._rootwindow.bind("<MouseWheel>", bajar_con_rueda)

        # Antes de dibujar: un lienzo con espacio de sobra para el mensaje
        filas = len(texto) // LETRAS_POR_FILA + texto.count("\n") + 1
        ajustar_lienzo(filas * ALTO_FILA - Y_INICIO)

        CLAVES[nombre](texto)

        # Después de dibujar: el lienzo justo del tamaño del dibujo
        x1, y1, x2, y2 = lienzo.bbox("all")   # y crece hacia abajo
        ajustar_lienzo(y2)

        # Guardar lo dibujado, para poder copiarlo como imagen
        if ruta_trazos:
            guardar_trazos(lienzo._canvas, ruta_trazos)

        turtle.mainloop()   # mantiene la ventanita abierta hasta que la cierren
    except (turtle.Terminator, tkinter.TclError):
        # Cerraron la ventanita antes de que terminara de dibujar:
        # no es un error, simplemente dejamos de dibujar
        pass