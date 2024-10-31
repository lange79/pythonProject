from random import shuffle

#lista inicial
palitos = ['-', '--', '---','----']

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#print(mezclar(palitos))

# pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento= input("Elegie un numero del 1 al 4:")
    return int(intento)


# comprobar intento

def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print("Perdiste")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezcaldos= mezclar(palitos)
seleccion= probar_suerte()
chequear_intento(palitos_mezcaldos, seleccion)

from random import randint

def lanzar_dados():
    nro1=randint(1,6)
    nro2=randint(1,6)
    resultado=evaluar_jugada(nro1,nro2)
    return resultado

def evaluar_jugada(n1,n2):
    suma_dados=n1+n2
    if suma_dados<=6:
        respuesta=f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 10<suma_dados >6:
        respuesta=f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        respuesta=f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    return respuesta

x='0'
while x!='S' and x!='N':
    jugar=input("Quieres jugar a los dados? s/n")
    x = jugar.upper()
if x=='S':
    print(lanzar_dados())









