lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice, item)
    indice +=1


lista = ['a','b','c']

for item in enumerate(lista):
    print(item)

for indice, item in enumerate(lista):
    print(indice, item)


for indice, item in enumerate(range(50,55)):
    print(indice, item)

lista = ['a','b','c']

mis_tuples = list(enumerate(lista))
print(mis_tuples)

mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

string ="Python"
lista_indices=list(enumerate(string))
print(lista_indices)


