# cifraClaves
_______________________________________________________________
Cifrado de diferentes claves guías y scouts con interfaz
Usando python qt y la biblioteca turtle.

Se encuentran las siguientes claves:

  - Murciélago   
  - Abuelito
  - Hipotenusa
  - Cenit Polar
  - Neumático
  - Parelinofu
  - Inversa
  - Malespín
  - Numérica
  - Fonética (Aún no)
  - Gato
  - China
  - Siete cruces
  - Musical 
  - Bailarín 
  - Morse

Para empaquetar en ejecutable windows correr en terminal:

si no está instalado el pyinstaller:
>>>python -m pip install pyinstaller

En la misma carpeta raíz del repo:
>>>python -m PyInstaller --noconfirm --windowed --name CodificadorScout --icon GUI/scouts.ico --add-data "GUI;GUI" main.py