from random import randint
aleatorio = randint(1,50)
print(aleatorio)

from random import *

aleatorio=uniform(1,5)
print(aleatorio)

aleatorio=round(uniform(1,5),1)
print(aleatorio)


aleatorio=random()
print(aleatorio)


colores=['azul','rojo','verde','amarillo']
aleatorio=choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)

import random
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo= random.choice(nombres)