import os

ruta = os.getcwd()

print(ruta)

Nueva_ruta = os.chdir('C:\\Users\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\Dia 6\\Nueva carpeta')
archivo=open("Otro_archivo.txt")
print(archivo.readline())

##ruta = os.makedirs("Nueva1")

#Nueva_ruta2 = os.makedirs('C:\\Users\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\Dia 6\\Nueva carpeta2\\prueba1')

ruta3 =  "'C:\\Users\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\Dia 6\\Nueva carpeta2\\prueba1"
elemento = os.path.basename(ruta3)
print(elemento)
elemento = os.path.dirname(ruta3)
print(elemento)
elemento = os.path.split(ruta3)
print(elemento)

#os.rmdir("C:\\Users\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\Dia 6\\Nueva carpeta\\Nueva1")


otro_archivo = open("C:\\Users\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\Dia 6\\Nueva carpeta\\Otro_archivo.txt")
print(otro_archivo.read())

from pathlib import Path

carpeta = Path("C:/Users/u599687/Downloads/Dev/PythonTotal/pythonProject/Dia 6/Nueva carpeta")
archivo=carpeta / "Otro_archivo.txt"
mi_archivo = open(archivo)
print(mi_archivo.read())

