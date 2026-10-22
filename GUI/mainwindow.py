"""
Created on Tue May 16 18:49:45 2023

@author: Irene

Ventana principal del programa
"""
import os
import subprocess
import sys
from PyQt5 import uic, QtWidgets

from claves.murcielago import claveMurcielago
from claves.inversa import claveABC
from claves.malespin import claveMalespin
from claves.numerica import claveNumerica
from claves.abuelito import claveAbuelito
from claves.cenitpolar import claveCenitPolar
from claves.hipotenusa import claveHipotenusa
from claves.neumatico import claveNeumatico
from claves.parelinofu import claveParelinofu
#from claves.fonetica import claveFonetica
from claves.morse import claveMorseTexto#, claveMorseDibujo

# Carpeta principal del proyecto (la que tiene main.py)
CARPETA_PROYECTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Si estamos dentro del ejecutable (.exe), PyInstaller deja los archivos (Principal.ui, imágenes) en sys._MEIPASS
# si no, están en el proyecto
CARPETA_ARCHIVOS = getattr(sys, "_MEIPASS", CARPETA_PROYECTO)

qtCreatorFile = os.path.join(CARPETA_ARCHIVOS, "GUI", "Principal.ui") # Nombre del archivo del QtDesigner

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        
        # Call the inherited classes __init__ method
        super(MyApp, self).__init__()

        # Load the .ui file
        uic.loadUi(qtCreatorFile, self)
        
        #_______________________________________________________________
        #Aquí van los botones
        self.boton_codificar.clicked.connect(self.codificando)
        self.boton_cerrar.clicked.connect(self.cerrando)
        #_______________________________________________________________

        self.proceso_dibujo = None   # la ventanita de dibujo abierta, si hay
        
            
    #Aquí van las funciones      
    #_______________________________________________________________    
    def cerrando(self):
        # Cierra la ventanita del dibujo, si hay una abierta
        if self.proceso_dibujo is not None and self.proceso_dibujo.poll() is None:
            self.proceso_dibujo.terminate()
        self.proceso_dibujo = None

    def closeEvent(self, event):
        # Al cerrar la ventana principal, cerramos también el dibujo
        self.cerrando()
        event.accept()

    def dibujar(self, clave, orig, nombre):
        # Cada dibujo corre en su propio proceso de Python (claves/dibujar.py),
        # así turtle y Qt no comparten ventanas ni se traban entre sí
        self.cerrando()   # si había un dibujo anterior, lo cerramos
        if getattr(sys, "frozen", False):
            # Dentro del .exe: el mismo ejecutable sabe dibujar
            comando = [sys.executable, "--dibujar", clave]
        else:
            # Desde VS Code: Python corre main.py en modo dibujo
            comando = [sys.executable, os.path.join(CARPETA_PROYECTO, "main.py"), "--dibujar", clave]
        self.proceso_dibujo = subprocess.Popen(
            comando,
            stdin=subprocess.PIPE,
            cwd=CARPETA_PROYECTO,
        )
        self.proceso_dibujo.stdin.write(orig.encode("utf-8"))
        self.proceso_dibujo.stdin.close()
        self.enClave.setText("En clave " + nombre + ", ver ventanita")

    def codificando(self):
        orig = self.original.toPlainText().upper()
        if self.rbtn_murcielago.isChecked() == True:
            self.enClave.setText(claveMurcielago(orig))
        elif self.rbtn_inversa.isChecked() == True:
            self.enClave.setText(claveABC(orig))
        elif self.rbtn_malespin.isChecked() == True:
            self.enClave.setText(claveMalespin(orig))
        elif self.rbtn_numerica.isChecked() == True:
            self.enClave.setText(claveNumerica(orig))
        elif self.rbtn_abuelito.isChecked() == True:
            self.enClave.setText(claveAbuelito(orig))
        elif self.rbtn_cenitpolar.isChecked() == True:
            self.enClave.setText(claveCenitPolar(orig))
        elif self.rbtn_hipotenusa.isChecked() == True:
            self.enClave.setText(claveHipotenusa(orig))
        elif self.rbtn_neumatico.isChecked() == True:
            self.enClave.setText(claveNeumatico(orig))
        elif self.rbtn_parelinofu.isChecked() == True:
            self.enClave.setText(claveParelinofu(orig))
        elif self.rbtn_gato.isChecked() == True:
            self.dibujar("gato", orig, "gato")
        elif self.rbtn_china.isChecked() == True:
            self.dibujar("china", orig, "china")
        elif self.rbtn_morse.isChecked() == True:
            #claveMorseDibujo(orig)
            self.enClave.setText(claveMorseTexto(orig))
        elif self.rbtn_bailarin.isChecked() == True:
            self.dibujar("bailarin", orig, "bailarín")
        elif self.rbtn_musical.isChecked() == True:
            self.dibujar("musical", orig, "musical")
        elif self.rbtn_sietecruces.isChecked() == True:
            self.dibujar("sietecruces", orig, "7 cruces")
        else:#claves que falten de programar
            self.enClave.setText("Aún no la he programado")
        
        '''
        elif self.rbtn_fonetica.isChecked() == True:
            self.enClave.setText(claveFonetica(orig))
        
        '''

    #_______________________________________________________________