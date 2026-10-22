"""
Created on Tue May 16 18:49:45 2023

@author: Irene

Ventana principal del programa
"""
import base64
import os
import subprocess
import sys
import tempfile
from PyQt5 import uic, QtCore, QtWidgets

from claves.murcielago import claveMurcielago
from claves.inversa import claveABC
from claves.malespin import claveMalespin
from claves.numerica import claveNumerica
from claves.abuelito import claveAbuelito
from claves.cenitpolar import claveCenitPolar
from claves.hipotenusa import claveHipotenusa
from claves.neumatico import claveNeumatico
from claves.parelinofu import claveParelinofu
from claves.fonetica import claveFonetica
from claves.morse import claveMorseTexto
from GUI.recorte import imagen_del_dibujo

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
        self.boton_cerrar.clicked.connect(self.cerrar_desde_boton)
        self.boton_copiar.clicked.connect(self.copiando)
        #_______________________________________________________________

        self.proceso_dibujo = None   # la ventanita de dibujo abierta, si hay
        self.archivo_dibujo = None   # donde la ventanita guarda lo dibujado (para copiarlo)
        self.numero_dibujo = 0       # para que cada dibujo use un archivo distinto
        
            
    #Aquí van las funciones      
    #_______________________________________________________________    
    def hay_dibujo_abierto(self):
        # True si la ventanita de dibujo sigue abierta
        # (poll() devuelve None mientras el proceso del dibujo siga vivo)
        return self.proceso_dibujo is not None and self.proceso_dibujo.poll() is None

    def cerrando(self):
        # Cierra la ventanita del dibujo, si hay una abierta
        if self.hay_dibujo_abierto():
            self.proceso_dibujo.terminate()
        self.proceso_dibujo = None

    def cerrar_desde_boton(self):
        # El botón "Cerrar ventana de clave": si no hay nada abierto, avisa
        if self.hay_dibujo_abierto():
            self.cerrando()
        else:
            self.avisar_en_boton(self.boton_cerrar, "¡Nada que\ncerrar!", "Cerrar ventana \nde clave")

    def copiando(self):
        # Copia al portapapeles, como si fuera Ctrl + C:
        #  - claves de texto: el texto codificado
        #  - claves dibujadas: la imagen del dibujo
        #  - Morse: las dos cosas (al pegar, cada programa usa la que le sirve)
        texto = self.enClave.toPlainText()
        if texto.endswith("ver ventanita"):
            texto = ""   # ese mensaje no es la clave: no se copia

        imagen = None
        if self.archivo_dibujo:
            imagen = imagen_del_dibujo(self.archivo_dibujo)
            if imagen is None and self.hay_dibujo_abierto():
                # Todavía no ha terminado de dibujar: aún no hay qué recortar
                self.avisar_en_boton(self.boton_copiar, "¡Aún dibujando!", "Copiar")
                return

        if texto == "" and imagen is None:
            self.avisar_en_boton(self.boton_copiar, "¡Nada que copiar!", "Copiar")
            return

        datos = QtCore.QMimeData()   # lo que se va a poner en el portapapeles
        if texto:
            datos.setText(texto)
        if imagen is not None:
            datos.setImageData(imagen)
        QtWidgets.QApplication.clipboard().setMimeData(datos)
        self.avisar_en_boton(self.boton_copiar, "¡Copiado!", "Copiar")

    def borrar_archivo_dibujo(self):
        # Borra el archivo temporal del dibujo anterior, si había uno
        if self.archivo_dibujo and os.path.exists(self.archivo_dibujo):
            try:
                os.remove(self.archivo_dibujo)
            except OSError:
                pass   # si Windows no lo deja borrar ahora, no pasa nada
        self.archivo_dibujo = None

    def avisar_en_boton(self, boton, aviso, texto_normal):
        # Muestra un aviso en el botón por 1.5 segundos y luego vuelve
        # a su texto de siempre (sirve para cualquier botón)
        boton.setText(aviso)
        QtCore.QTimer.singleShot(1500, lambda: boton.setText(texto_normal))

    def closeEvent(self, event):
        # Al cerrar la ventana principal, cerramos también el dibujo
        # y borramos su archivo temporal
        self.cerrando()
        self.borrar_archivo_dibujo()
        event.accept()

    def dibujar(self, clave, orig, nombre):
        # Cada dibujo corre en su propio proceso de Python (claves/dibujar.py),
        # así turtle y Qt no comparten ventanas ni se traban entre sí
        self.cerrando()   # si había un dibujo anterior, lo cerramos
        # El texto viaja en base64 (solo letras y números) para que tildes,
        # comillas y cambios de línea no se rompan en el camino
        texto64 = base64.urlsafe_b64encode(orig.encode("utf-8")).decode("ascii")
        # Archivo temporal donde la ventanita va a guardar lo que dibujó,
        # para poder copiarlo como imagen (se borra el del dibujo anterior)
        self.borrar_archivo_dibujo()
        self.numero_dibujo += 1
        self.archivo_dibujo = os.path.join(tempfile.gettempdir(),
                                           "cifraClaves_%d_dibujo%d.json" % (os.getpid(), self.numero_dibujo))
        if getattr(sys, "frozen", False):
            # Dentro del .exe: el mismo ejecutable sabe dibujar
            comando = [sys.executable, "--dibujar", clave, texto64, self.archivo_dibujo]
        else:
            # Desde VS Code: Python corre main.py en modo dibujo
            comando = [sys.executable, os.path.join(CARPETA_PROYECTO, "main.py"), "--dibujar", clave, texto64, self.archivo_dibujo]
        self.proceso_dibujo = subprocess.Popen(comando, cwd=CARPETA_PROYECTO)
        self.enClave.setText("En clave " + nombre + ", ver ventanita")


    def codificando(self):
        orig = self.original.toPlainText().upper()   # todo en mayúscula para que la salida quede pareja
        self.borrar_archivo_dibujo()   # el dibujo anterior ya no es lo que se va a copiar
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
        elif self.rbtn_fonetica.isChecked() == True:
            self.enClave.setText(claveFonetica(orig))    
        elif self.rbtn_gato.isChecked() == True:
            self.dibujar("gato", orig, "gato")
        elif self.rbtn_china.isChecked() == True:
            self.dibujar("china", orig, "china")
        elif self.rbtn_morse.isChecked() == True:
            self.dibujar("morse", orig, "morse")
            self.enClave.setText(claveMorseTexto(orig))
        elif self.rbtn_bailarin.isChecked() == True:
            self.dibujar("bailarin", orig, "bailarín")
        elif self.rbtn_musical.isChecked() == True:
            self.dibujar("musical", orig, "musical")
        elif self.rbtn_sietecruces.isChecked() == True:
            self.dibujar("sietecruces", orig, "7 cruces")
        else:#claves que falten de programar
            self.enClave.setText("Aún no la he programado")
    #_______________________________________________________________