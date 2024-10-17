lista = ['a','b','c']

for letra in lista:
        print(letra)


lista = ['a','b','c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista=['pablo','laura','fede','luis','julia']

for nombre in lista:
    if nombre.startswith('l'):
        print("Nombres que comienzan con L:", nombre)
    else:
        print('Nombres que no comienzan con L:', nombre)


numeros = [1,2,3,4,5]
mi_valor=0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)


palabra ='python'
for letra in palabra:
    print(letra)


palabra ='python'
for letra in palabra:
    print(letra)

for letra in 'python es genial':
    print(letra)

for numero in [1,2,3]:
    print(numero)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {'clave1':'a', 'clave2':'b','clave3':'c'}
for item in dic:
    print(item)


dic = {'clave1':'a', 'clave2':'b','clave3':'c'}
for item in dic.items():
    print(item)

dic = {'clave1':'a', 'clave2':'b','clave3':'c'}
for item in dic.values():
    print(item)


dic = {'clave1':'a', 'clave2':'b','clave3':'c'}
for a,b in dic.items():
    print(a,b)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumno in alumnos_clase:
    print(f"Hola {alumno}")


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros+numero


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if (numero%2==0):
        suma_pares=suma_pares+numero
    else:
        suma_impares=suma_impares+numero