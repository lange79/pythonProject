"""import zipfile

mi_zip=zipfile.ZipFile("archivo_comprimido.zip","w")

mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")

mi_zip.close()"""

"""import zipfile

zip_abierto=zipfile.ZipFile("archivo_comprimido.zip","r")

zip_abierto.extractall()"""

"""import shutil

carpeta_origen = "C:\\Users\\u599687\\Downloads\\Dev\\PythonTotal\\pythonProject\\Dia 9\\Prueba1"
archivo_destino = "Todo_Comprimido"
shutil.make_archive(archivo_destino,"zip",carpeta_origen)"""



import shutil

shutil.unpack_archive("Todo_Comprimido.zip", "extracion terminada", "zip")

