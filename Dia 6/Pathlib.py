from pathlib import Path
carpeta = Path("C:/Users/u599687/Downloads/Dev/PythonTotal/pythonProject/Dia 6/Nueva carpeta/Otro_archivo.txt")
print(carpeta.read_text())

print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)


carpeta = Path("C:/Users/u599687/Downloads/Dev/PythonTotal/pythonProject/Dia 6/Nueva carpeta/Otro_archivo2.txt")

if not carpeta.exists():
    print("Este Archivo NO Existe")
else:
    print("Este Archivo SI Existe")

from pathlib import PureWindowsPath

carpeta = Path("C:/Users/u599687/Downloads/Dev/PythonTotal/pythonProject/Dia 6/Nueva carpeta/Otro_archivo.txt")

ruta_windows=PureWindowsPath(carpeta)

print(ruta_windows)
