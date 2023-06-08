"""
Created on Tue May 16 18:49:45 2023

@author: Irene

Ventana principal del programa
"""
import sys
from PyQt5 import uic, QtWidgets
import turtle

from claves.murcielago import claveMurcielago
from claves.inversa import claveABC
from claves.malespin import claveMalespin
from claves.numerica import claveNumerica
from claves.CifrarGato import claveGato
from claves.abuelito import claveAbuelito
from claves.cenitpolar import claveCenitPolar
from claves.hipotenusa import claveHipotenusa
from claves.neumatico import claveNeumatico
from claves.parelinofu import claveParelinofu
#from claves.fonetica import claveFonetica
from claves.CifrarChina import claveChina
from claves.CifrarSietecruces import claveSieteCruces
from claves.CifrarMusical import claveMusical
from claves.CifrarBailarin import claveBailarin
from claves.morse import claveMorseTexto#, claveMorseDibujo

qtCreatorFile = "./GUI/Principal.ui" # Nombre del archivo del QtDesigner

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
        
            
    #Aquí van las funciones      
    #_______________________________________________________________    
    def cerrando(self):
        try:    
            turtle.bye()   
        except turtle.Terminator:
            pass
    
    
    def codificando(self):
        orig = self.original.toPlainText()
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
            claveGato(orig)
            self.enClave.setText("En clave gato, ver ventanita")
        elif self.rbtn_china.isChecked() == True:
            claveChina(orig)
            self.enClave.setText("En clave china, ver ventanita")
        elif self.rbtn_morse.isChecked() == True:
            #claveMorseDibujo(orig)
            self.enClave.setText(claveMorseTexto(orig))
        elif self.rbtn_bailarin.isChecked() == True:
            claveBailarin(orig)
            self.enClave.setText("En clave bailarín, ver ventanita")
        elif self.rbtn_musical.isChecked() == True:
            claveMusical(orig)
            self.enClave.setText("En clave musical, ver ventanita")
        elif self.rbtn_sietecruces.isChecked() == True:
            claveSieteCruces(orig)
            self.enClave.setText("En clave 7 cruces, ver ventanita")
        else:#claves que falten de programar
            self.enClave.setText("Aún no la he programado")
        
        '''
        elif self.rbtn_fonetica.isChecked() == True:
            self.enClave.setText(claveFonetica(orig))
        
        '''

    #_______________________________________________________________    