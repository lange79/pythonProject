"""from random import randint

def lanzar_dados():
    nro1=randint(1,6)
    nro2=randint(1,6)
    return nro1,nro2


def evaluar_jugada(n1,n2):
    suma_dados=n1+n2
    respuesta=''
    if suma_dados<=6:
        respuesta=f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 10<suma_dados >6:
        respuesta=f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados>=10:
        respuesta=f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    return respuesta

num1,num2=lanzar_dados()
print(num1,num2)
resultado=evaluar_jugada(num1,num2)
print(resultado)"""



"""def reducir_lista(lista):
    lista=list(set(lista))
    lista.pop()
    print(lista)
    return lista

def promedio (num):
    suma=0
    cant=len(num)
    for n in num:
        suma=suma+n
    prom=suma/cant
    return prom

lista_numeros=[1,2,15,7,2]
numeros=reducir_lista(lista_numeros)
print(promedio(numeros))"""

import random


def lanzar_moneda():
    opciones = ['Cara', 'Cruz']
    coc = random.choice(opciones)
    return coc


def probar_suerte(moneda, numeros):
    if moneda == 'Cara':
        print("La lista se autodestruira")
        numeros = []
    else:
        print("La lista fue salvada")
    return numeros


lista_numeros = [1, 3, 4, 8, 7, 15, 2]
print("La lista es:",lista_numeros)
moneda = lanzar_moneda()
probar_suerte(moneda, lista_numeros)
print("La lista quedo asi:",lista_numeros)


