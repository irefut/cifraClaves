# cifraClaves
_______________________________________________________________
Cifrado de diferentes claves guías y scouts con interfaz
Programado en Python 3. Usando python qt y la biblioteca turtle.

Tenemos algunas que son de texto(T) y otras de dibujo(D).

Se encuentran las siguientes claves:

  - Murciélago   (T)
  - Abuelito     (T)
  - Hipotenusa   (T)
  - Cenit Polar  (T)
  - Neumático    (T)
  - Parelinofu   (T)
  - Inversa      (T)
  - Malespín     (T)
  - Numérica     (T)
  - Fonética     (T)
  - Gato         (D)
  - China        (D)
  - Siete cruces (D)
  - Musical      (D)
  - Bailarín     (D)
  - Morse        (T)(D)

Requerimientos técnicos necesarios:
-PyQt5

## Instalar

Al trabajar en una PC diferente correr:
```
python -m pip install -r requerimientos.txt
```

## Correr el programa

Desde la raíz del repo corremos:
```
python main.py
```

## Generar ejecutable para Windows

Para empaquetar en ejecutable para Windows correr en terminal:

si no está instalado el pyinstaller:
```
python -m pip install pyinstaller
```

Ahora sí, para generar el archivo ejecutable, nos paramos en la misma carpeta raíz del repo:
```
python -m PyInstaller --noconfirm --windowed --name CodificadorScout --icon GUI/scouts.ico --add-data "GUI;GUI" main.py
```

El programa queda en `dist/CodificadorScout/`. Para pasarlo a otra compu,
se comprime **toda esa carpeta** en un .zip; en la otra compu se descomprime
y se abre `CodificadorScout.exe` (no necesita Python instalado)

## Estructura

```
main.py              Abre la ventana principal (o, con --dibujar, solo un dibujo)
GUI/
  mainwindow.py      Lógica de la ventana principal
  recorte.py         Arma la imagen de una clave dibujada para el botón Copiar
  Principal.ui       Diseño de la ventana (se edita con Qt Designer)
  *.png, *.ico       Logos e ícono
claves/
  dibujar.py         Abre la ventanita de dibujo en un proceso aparte
  sustitucion.py     Lo que comparten las claves de texto: cada una solo define su tabla
  Cifrar*.py         Claves con dibujo (turtle)
  *.py               Claves de texto
```