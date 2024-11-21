"""
def cambiar_letras(tipo):

    print("Entre a cambiar letras.")
    print("esto hay en tipo:",tipo)

    def mayuscula(texto):
        print("Entre a funcion Mayuscula en Cambiar letras")
        print("esto hay en tipo:", tipo)
        print("Esto hay en texto:", texto)
        print(texto.upper())

    def minuscula(texto):
        print("Entre a funcion Minuscula en Cambiar letras")
        print("esto hay en tipo:", tipo)
        print("Esto hay en texto:", texto)
        print(texto.lower())


    if tipo=="may":
        print("Entre a IF May")
        return mayuscula
    elif tipo == "min":
        print("Entre a IF Min")
        return minuscula


operacion = cambiar_letras("may")
print("Este es el print posterior a operacion = cambiar_letras",operacion.__str__())
operacion("palabra")
print("Este es el print posterior a operacion = ('palabra')",operacion.__str__())


 def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

@decorar_saludo
def minuscula(texto):
    print(texto.lower())

minuscula("Python")

"""

def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula("diego")
mayuscula_decorada("diego")