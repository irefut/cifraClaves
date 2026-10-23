"""
Ventanita de instrucciones: explica cómo se usa el programa.

El texto está escrito en HTML (el mismo lenguaje de las páginas web), así
se le puede dar formato: <b>negrita</b>, listas con <ul><li>...</li></ul>,
títulos con <h3>, etc. Para cambiar la explicación, basta con editar
el texto de INSTRUCCIONES.
"""
from PyQt5 import QtWidgets

INSTRUCCIONES = """
<h2><u>Cómo usar el codificador</u></h2>

<ol>
  <li>Escribe el mensaje en <b>Texto a codificar</b>.</li>
  <li>Elige la clave en la lista <b>En clave</b>.</li>
  <li>Toca <b>Codificar</b>.</li>
</ol>

<h3>Claves de texto</h3>
<p>Murciélago, Abuelito, Hipotenusa, Cenit Polar, Neumático, Parelinofu,
Inversa, Malespín, Numérica y Fonética: el mensaje en clave aparece en el
cuadro de <b>Texto codificado</b>.</p>

<h3>Claves con dibujo</h3>
<p>Gato, China, Siete Cruces, Musical y Bailarín: se abre una ventanita
aparte donde se dibuja la clave.</p>

<p><b>Morse</b> sale de las dos formas: en texto en el cuadro de abajo
y dibujada en la ventanita.</p>

<h3>Copiar</h3>
<p>El botón <b>Copiar</b> copia el resultado para pegarlo donde quieras
(WhatsApp, Word, un correo...) con <b>Ctrl + V</b>:</p>
<ul>
  <li>En las claves de texto copia el texto.</li>
  <li>En las claves con dibujo copia una <b>imagen</b> del dibujo completo.
      Espera a que termine de dibujar antes de copiar.</li>
</ul>
"""


def mostrar_instrucciones(ventana_principal):
    """Abre la ventanita de instrucciones encima de la ventana principal."""
    dialogo = QtWidgets.QDialog(ventana_principal)
    dialogo.setWindowTitle("Instrucciones")
    dialogo.resize(520, 505)
    dialogo.setStyleSheet("background-color: rgb(255, 232, 222);")   # mismo color que la principal

    # Cuadro con el texto (si no cabe, aparece la barra para bajar)
    texto = QtWidgets.QTextBrowser()
    texto.setHtml(INSTRUCCIONES)
    # Sin borde y del mismo celeste que la ventana: así parece que el texto
    # está escrito directo en la ventana y no dentro de un cuadro
    texto.setFrameShape(QtWidgets.QFrame.NoFrame)
    texto.setStyleSheet("background-color: rgb(255, 232, 222); border: none; font-size: 10pt;")

    # Botón para cerrar
    botones = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)
    botones.button(QtWidgets.QDialogButtonBox.Ok).setText("Entendido")
    botones.button(QtWidgets.QDialogButtonBox.Ok).setStyleSheet("background-color: rgb(227, 182, 161); padding: 4px 16px; font-size: 11pt;")
    botones.accepted.connect(dialogo.accept)

    # Acomodar el texto arriba y el botón abajo
    acomodo = QtWidgets.QVBoxLayout(dialogo)
    acomodo.addWidget(texto)
    acomodo.addWidget(botones)

    dialogo.exec_()   # se queda abierta hasta que toquen "Entendido" o la X
