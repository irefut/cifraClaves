# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:28:05 2023

@author: Irene

Versión 3.4

Se puede abrir de dos formas:
    python main.py                    -> abre la ventana principal
    python main.py --dibujar gato <texto> <archivo>  -> solo dibuja una clave con turtle
                                                        (lo usa la ventana principal)
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[1] == "--dibujar":
        # Modo dibujo: lo abre la ventana principal para cada clave con dibujo
        from claves.dibujar import dibujar_desde_texto64
        ruta_trazos = sys.argv[4] if len(sys.argv) >= 5 else None
        dibujar_desde_texto64(sys.argv[2], sys.argv[3], ruta_trazos)
    else:
        from PyQt5 import QtCore, QtGui, QtWidgets
        from GUI.mainwindow import MyApp

        # En pantallas con zoom (125 %, 150 %) Qt agranda las letras, pero no las posiciones
        # fijas de Qt Designer, y todo queda apretado. Con esto Qt agranda todo parejo
        if hasattr(QtGui.QGuiApplication, "setHighDpiScaleFactorRoundingPolicy"):
            QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
                QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())