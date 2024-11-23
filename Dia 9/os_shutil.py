import os
from time import sleep

print(os.getcwd())

archivo = open("curso.txt", "w")
archivo.write("texto de prueba")
archivo.close()

print(os.listdir())

import shutil

#shutil.move("curso.txt", "c:\\Users\\u599687\\Desktop")

import send2trash


#sleep(5)
#send2trash.send2trash("curso.txt")

print(os.walk("c:\\User\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\Dia 9\\"))

ruta = os.getcwd()
print(os.walk("c:\\User\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\"))

os.path


for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for arch in archivo:
        if arch.startswith("prue"):
            print(f"\t{arch}")
    print("\n")



