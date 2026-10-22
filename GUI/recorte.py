# -*- coding: utf-8 -*-
"""
Arma la imagen (el "recorte") de una clave dibujada, para copiarla.

La ventanita de dibujo (claves/dibujar.py) guarda en un archivo la lista
de todo lo que dibujó: líneas, figuras rellenas y textos. Aquí se lee esa
lista y se vuelve a dibujar todo en una imagen de Qt, recortada justo al
tamaño del dibujo. Así sale completa aunque el mensaje sea largo y en la
ventanita haya que bajar con la barra.
"""
import json
import os

from PyQt5 import QtCore, QtGui

MARGEN = 20    # espacio en blanco alrededor del dibujo, en píxeles
ESCALA = 2     # se dibuja al doble de tamaño para que se vea nítido al pegarlo


def imagen_del_dibujo(ruta):
    """Devuelve la imagen del dibujo guardado en 'ruta', o None si todavía
    no existe (porque aún está dibujando o lo cerraron antes de terminar)."""
    if not ruta or not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as archivo:
        trazos = json.load(archivo)
    if not trazos:
        return None

    # Hasta dónde llega el dibujo hacia cada lado
    xs, ys = [], []
    for trazo in trazos:
        if trazo["tipo"] == "texto":
            x1, y1, x2, y2 = trazo["caja"]
            xs += [x1, x2]
            ys += [y1, y2]
        else:
            grosor = trazo["ancho"] / 2   # las líneas gruesas se salen un poco de sus puntos
            for x in trazo["puntos"][0::2]:
                xs += [x - grosor, x + grosor]
            for y in trazo["puntos"][1::2]:
                ys += [y - grosor, y + grosor]
    izquierda = min(xs) - MARGEN
    arriba = min(ys) - MARGEN
    ancho = max(xs) + MARGEN - izquierda
    alto = max(ys) + MARGEN - arriba

    # Una imagen en blanco del tamaño justo
    imagen = QtGui.QImage(int(ancho * ESCALA), int(alto * ESCALA), QtGui.QImage.Format_RGB32)
    imagen.fill(QtCore.Qt.white)

    pintor = QtGui.QPainter(imagen)
    pintor.setRenderHint(QtGui.QPainter.Antialiasing)       # bordes suaves
    pintor.setRenderHint(QtGui.QPainter.TextAntialiasing)
    pintor.scale(ESCALA, ESCALA)
    pintor.translate(-izquierda, -arriba)   # que la esquina del dibujo quede en (0, 0)

    for trazo in trazos:   # en el mismo orden en que se dibujaron
        if trazo["tipo"] == "linea":
            dibujar_linea(pintor, trazo)
        elif trazo["tipo"] == "poligono":
            dibujar_poligono(pintor, trazo)
        elif trazo["tipo"] == "texto":
            dibujar_texto(pintor, trazo)

    pintor.end()
    return imagen


def lista_de_puntos(numeros):
    # [x1, y1, x2, y2, ...] -> [QPointF(x1, y1), QPointF(x2, y2), ...]
    return [QtCore.QPointF(numeros[i], numeros[i + 1]) for i in range(0, len(numeros) - 1, 2)]


def dibujar_linea(pintor, trazo):
    puntos = lista_de_puntos(trazo["puntos"])
    grosor = max(trazo["ancho"], 1)
    color = QtGui.QColor(trazo["color"])

    xs = [p.x() for p in puntos]
    ys = [p.y() for p in puntos]
    if max(xs) - min(xs) < 0.5 and max(ys) - min(ys) < 0.5:
        # Línea sin largo: turtle la usa para hacer puntos redondos
        pintor.setPen(QtCore.Qt.NoPen)
        pintor.setBrush(color)
        pintor.drawEllipse(puntos[0], grosor / 2, grosor / 2)
        pintor.setBrush(QtCore.Qt.NoBrush)
        return

    lapiz = QtGui.QPen(color)
    lapiz.setWidthF(grosor)
    lapiz.setCapStyle(QtCore.Qt.RoundCap)     # puntas redondas, como turtle
    lapiz.setJoinStyle(QtCore.Qt.RoundJoin)
    pintor.setPen(lapiz)
    pintor.drawPolyline(QtGui.QPolygonF(puntos))


def dibujar_poligono(pintor, trazo):
    if trazo["borde"]:
        lapiz = QtGui.QPen(QtGui.QColor(trazo["borde"]))
        lapiz.setWidthF(max(trazo["ancho"], 1))
        pintor.setPen(lapiz)
    else:
        pintor.setPen(QtCore.Qt.NoPen)
    if trazo["relleno"]:
        pintor.setBrush(QtGui.QColor(trazo["relleno"]))
    else:
        pintor.setBrush(QtCore.Qt.NoBrush)
    pintor.drawPolygon(QtGui.QPolygonF(lista_de_puntos(trazo["puntos"])))
    pintor.setBrush(QtCore.Qt.NoBrush)


def dibujar_texto(pintor, trazo):
    fuente = QtGui.QFont(trazo["familia"])
    fuente.setPixelSize(max(trazo["pixeles"], 1))
    fuente.setBold(trazo["negrita"])
    pintor.setFont(fuente)
    pintor.setPen(QtGui.QColor(trazo["color"]))
    x1, y1, x2, y2 = trazo["caja"]
    # Centrado en el mismo rectángulo que ocupaba en la ventanita
    pintor.drawText(QtCore.QRectF(x1, y1, x2 - x1, y2 - y1), QtCore.Qt.AlignCenter, trazo["texto"])
