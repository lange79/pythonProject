

def elegir_letra ():
    letra=input("Ingrese la letra que cree que se encuentra en las palabra a adivinar:").lower()
    while 'a'>letra>'z':
        letra = input("Ingrese la letra que cree que se encuentra en las palabra a adivinar:").lower()
    return letra


def busca_acierto(let, pal, pal_sec, vid):
    x=len(palabra)
    for n in range(x):
        if pal[n]==let:
            pal_sec[n]=let
    print(pal_sec)

    return vid
    return vid-1



from random import choice
diccionario=['perro', 'gato', 'alumno','escoba', 'doctor','barrilete', 'edificio']
palabra=choice(diccionario)
print(palabra)
largo_p=len(palabra)
vidas=6
cont=0
palabra_secreta=[]
for n in palabra:
    print(cont)
    palabra_secreta.append('-')
    cont += 1
print("bienvenido al juego del ahorcado")
print("la palabra a adivinar es:", palabra_secreta)
while vidas>0:
    letra = elegir_letra()
    vidas=busca_acierto(letra, palabra, palabra_secreta,vidas)




        #palabra_secreta[posicion_letra]=letra
        #print(f"Acertaste, la letra {letra} se encuentra en la palabra!")
        #print("La palabra a adivinar es:",list(palabra_secreta))

    #vidas -= 1