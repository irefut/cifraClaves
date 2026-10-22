# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:28:05 2023

@author: Irene

Versión 4.0

Se puede abrir de dos formas:
    python main.py                    -> abre la ventana principal
    python main.py --dibujar gato     -> solo dibuja una clave con turtle
                                         (lo usa la ventana principal)
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--dibujar":
        # Modo dibujo: lo abre la ventana principal para cada clave con dibujo
        from claves.dibujar import dibujar_desde_stdin
        dibujar_desde_stdin(sys.argv[2])
    else:
        # Modo normal: la ventana principal
        from PyQt5 import QtWidgets
        from GUI.mainwindow import MyApp

        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())