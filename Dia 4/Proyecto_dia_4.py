jugador=input("Ingrese su nombre:")
print(f"Hola {jugador}, he pensado un numero entre 1 y 100, tienes 8 intentos para adivinar cual crees que es el numero")
from random import randint
numero=randint(1,100)
intentos=1
while intentos in range(1,9):
    numero_Jugador = int(input("Ingrese el numero que cree que he pensado: "))
    if 0<numero_Jugador<=100:
        if numero_Jugador==numero:
            print(f"Felicidades {jugador} has adivinado el numero en {intentos} intentos!!")
            break
        elif numero_Jugador<numero:
            print(f"Incorrecto {jugador}!. El numero elegido es menor al numero que he pensado."
                  f"Te quedan {8-intentos} intentos")
        else:
            print(f"Incorrecto {jugador}!. El numero elegido es mayor al numero que he pensado."
                  f"Te quedan {8-intentos} intentos")
    else:
        print(f"Lo siento {jugador}, has elegido un numero que no esta permitido.")
        continue
    intentos+=1
print(f"Lo siento {jugador} se te han acabado los intentos.")






