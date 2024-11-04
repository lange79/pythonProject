
def elegir_letra():
    letra = input("\nIngrese la letra (A-Z)que cree que se encuentra en la palabra a adivinar:").lower()
    while letra > 'z' or letra < 'a' or len(letra)!=1:
        print("\n\nLa letra elegida no se encuentra entre la A y la Z.")
        letra = input("\nIngrese la letra (A-Z) que cree que se encuentra en las palabra a adivinar:").lower()
    return letra


def busca_acierto(let, pal, pal_sec, vid, letras_equivocadas):
    x = len(pal)
    cont = 0
    for n in range(x):
        if pal[n] == let:
            pal_sec[n] = let
            cont += 1


    if cont == 0:
        vid -= 1
        letras_equivocadas.append(let)
        print(f"\nLo siento, la letra '{let}' no se encuentra en la palabra.\nTe quedan {vid} vidas!")
        print("\nLa palabra a adivinar es:\n",list(pal_sec))
        return vid, pal_sec,letras_equivocadas

    else:
        print(f"\nAcertaste, la letra '{let}' se encuentra en la palabra!")
        print("\nLa palabra a adivinar es:\n",list(pal_sec))
        return vid, pal_sec,letras_equivocadas


from random import choice

diccionario = ['cafetera','computadora','avion','helicoptero','perro', 'gato', 'alumno', 'escoba', 'doctor', 'barrilete', 'edificio']
palabra = choice(diccionario)

lista_palabra = []
for letra in palabra:
    lista_palabra.append(letra)

largo_p = len(lista_palabra)
vidas = 6
cont = 0
palabra_secreta = []
letras_erroneas= []
for n in lista_palabra:
    palabra_secreta.append('-')
    cont += 1
print("\nbienvenido al juego del ahorcado\n")
print("\nla palabra a adivinar es:\n\n", palabra_secreta)
while vidas > 0 and lista_palabra != palabra_secreta:
    letra = elegir_letra()
    vidas, palabra_secreta, letras_erroneas = busca_acierto(letra, lista_palabra, palabra_secreta, vidas, letras_erroneas)
    print("\nLa lista de letras que no forman la palabra es:\n", letras_erroneas)

if vidas==0:
    print("\n\nLos siento, se te acabaron las vidas.\nHas Perdido.")
else:
    print("\n\nFelicitaciones, descubriste la palabra.\nHaz ganado el juego!")