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
python -m PyInstaller --noconfirm --onefile --noupx --windowed --name CodificadorClavesGuiaScout --icon GUI/scouts.ico --version-file version_info.txt --add-data "GUI;GUI" main.py
```

El programa queda en `dist/CodificadorScout/`. Para pasarlo a otra compu, se comprime **toda esa carpeta** en un .zip; en la otra compu se descomprime y se abre `CodificadorScout.exe` 

## Estructura

```
main.py              Abre la ventana principal (o, con --dibujar, solo un dibujo)
GUI/
  mainwindow.py      Lógica de la ventana principal
  recorte.py         Arma la imagen de una clave dibujada para el botón Copiar
  instrucciones.py   Texto de la ventanita de Instrucciones
  Principal.ui       Diseño de la ventana (se edita con Qt Designer)
  *.png, *.ico       Logos e ícono
claves/
  dibujar.py         Abre la ventanita de dibujo en un proceso aparte
  sustitucion.py     Lo que comparten las claves de texto: cada una solo define su tabla
  Cifrar*.py         Claves con dibujo (turtle)
  *.py               Claves de texto
```

## Cómo se usa

1. Escribe el mensaje en **Texto a codificar**, elige la clave y toca **Codificar**.
2. Las claves de texto muestran el resultado abajo; las de dibujo abren una ventanita aparte.
3. **Copiar** copia el resultado: el texto, o la imagen del dibujo en las claves dibujadas.
   La ventanita de dibujo también tiene su propio botón **Copiar dibujo**.
4. **Instrucciones** abre una ventanita con la explicación completa.