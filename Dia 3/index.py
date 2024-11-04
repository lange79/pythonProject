#mi_texto = "esta es una prueba"
#resultado = mi_texto[-4]
#print(resultado)


mi_texto = "esta es una prueba"
resultado = mi_texto.index("a", 1, 5)
print(resultado)

mi_texto = "esta es una prueba"
resultado = mi_texto.rindex("a")
print(resultado)

frase = "Controlar la complejidad es la esencia de la programación"
slicing = frase[0:9]
print (slicing)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
slicing=frase[9::3]
print(slicing)