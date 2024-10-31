def suma(a,b):
    return a+b

print(suma(5,6))


def suma(*args):
    total=0

    for arg in args:
        total += arg
    return total

print(suma(5,100,55))

def suma(*args):
    return sum(args)

print(suma(suma(5,14,22,37)))


def suma_cuadrados(*args):
    suma=0
    for i in args:
        suma += i**2
    return suma

print(suma_cuadrados(1,2,3))


def numeros_persona(nom, *args):
    suma_numeros=sum(args)
    respuesta=f"{nom}. la suma de tus números es {suma_numeros}"
    return respuesta


nombre='Diego'
numeros=(1,3,5,2)
numeros_persona(nombre, numeros)