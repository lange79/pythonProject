def multiplicar(numero1, numero2):
    total = numero1*numero2
    return total

resultado =multiplicar(5,10)
print(resultado)


def usd_eur(dolares):
    return (dolares*0.9)


dolares = 60
eu = usd_eur(dolares)
print(eu)

dolares = 1200


def usd_a_eur(dolares):
    return dolares * 0.90



def invertir_palabra(palabra):
    print(palabra)
    palabra = palabra[::-1]
    print(palabra)
    palabra = palabra.upper()
    print(palabra)
    return palabra

palabra = "Curso de Python"
invertir_palabra(palabra)

