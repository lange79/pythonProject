texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto[2].upper()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.lower()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split()
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split("t")
print(resultado)

a= "Aprender"
b= "Python"
c= "es"
d= "genial"
e = "-".join([a,b,c,d])
print(e)


texto = "Este es el texto de Federico"
resultado = texto.find("s")
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.find("g")
print(resultado)


texto = "Este es el texto de Federico"
resultado = texto.replace("Federico", "todos")

print(resultado)


lista_palabras = ["La","legibilidad","cuenta."]
resultado=" ".join(lista_palabras)
print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil","fácil")
resultado = resultado.replace("mala","buena")
print(resultado)