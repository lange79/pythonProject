mi_lista = ['a','b','c']
otra_lista =['hola', 55,6.1]
print(type(mi_lista))
print(otra_lista)
resultado=len(mi_lista)
print(resultado)

resultado=mi_lista[0]
print(resultado)
resultado=mi_lista[0:1]
print(resultado)
mi_lista2=['d','e','f']
print(mi_lista+mi_lista2)

mi_lista3=mi_lista+mi_lista2
print(mi_lista3)

mi_lista3[0]='alfa'
print(mi_lista3)

mi_lista3.append('g')
print(mi_lista3)
mi_lista3.pop()
print("pop",mi_lista3)
mi_lista3.pop(0)
print("pop0",mi_lista3)

eliminado= mi_lista3.pop(0)
print(mi_lista3)
print(eliminado)

lista = ['g', 'o','b','m','c']
lista.sort()
print("ordenada",lista)

lista = ['g', 'o','b','m','c']
nueva_lista=lista.sort()
print(nueva_lista)
print(type(nueva_lista))

lista.reverse()
print(lista)


