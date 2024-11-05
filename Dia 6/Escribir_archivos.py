archivo = open('Prueba1.txt', 'w')
archivo.write('Soy el nuevo texto\n')
archivo.write('Soy el nuevo texto 2\n')
archivo.writelines(['Hola','mundo','aqui','estoy','\n'])
lista= ['Hola','mundo','aqui','estoy']
for p in lista:
    archivo.writelines(p + '\n' )

archivo.write('''\nEste es un texto de varias
lineas, que va a ocupar 3 renglones,
siendo este el ultimo\n''')
archivo.close()

archivo = open('Prueba1.txt', 'a')
archivo.write('\nAhora esta es la ultima linea')
#archivo.close()

archivo=open("registro.txt","a")
registro_ultima_sesion = ["Federico", "22/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo.write("\n")
for p in registro_ultima_sesion:
    archivo.writelines(p+"\t")

archivo.close()
archivo=open("registro.txt","r")
print(archivo.read())