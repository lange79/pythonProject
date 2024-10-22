def chequear_3_cifras(numero):
    return numero in range (100,1000)

suma=65+40
resultado=chequear_3_cifras(suma)
print(resultado)


def chequear_3_cifras(lista):
    for n in lista:
        if n in range (100,1000):
            return True
        else:
            pass
    return False

resultado=chequear_3_cifras([55,99,60])
print(resultado)


def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range (100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado=chequear_3_cifras([55,99,600])
print(resultado)


def todos_positivos(lista):
    lista_numeros = []
    result=True
    for n in lista:
        if n > 0:
            lista_numeros.append(n)
        else:
            result=False
    print(lista_numeros)
    return result


resultado= todos_positivos([50,1,101])
print(resultado)