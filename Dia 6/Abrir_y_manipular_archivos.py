mi_archivo = open('archivo.txt')
print (mi_archivo)
print(mi_archivo.read())


mi_archivo = open('Prueba.txt')

print(mi_archivo.readline())

una_linea=mi_archivo.readline()
print(una_linea.rstrip())

una_linea=mi_archivo.readline()
print(una_linea.upper())

mi_archivo = open('Prueba.txt')

todas=mi_archivo.readlines()
print(todas)



mi_archivo = open('Prueba.txt')


for l in mi_archivo:
    print ("Aqui dice: " + l)

mi_archivo = open('Prueba.txt')
todas=mi_archivo.readlines()
todas=todas.pop()
print (todas)

mi_archivo = open('Prueba.txt')
segunda=mi_archivo.readlines()
print(str(segunda[1]))


mi_archivo.close()