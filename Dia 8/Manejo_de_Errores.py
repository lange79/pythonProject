"""def suma():
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    print(n1+n2)
    print("Gracias por Sumar!")


try:
    suma()
except:
    print("Algo no ha salido bien")
else:
    print("Hiciste todo bien!")
finally:
    print("Eso fue todo")

try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    print("Hiciste todo bien!")
finally:
    print("Eso fue todo")"""


def pedir_numero():
    while True:
        try:
            numero=int(input("Dame un Numero:"))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")


pedir_numero()


