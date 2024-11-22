"""def generador():
    x=0
    while x!=-1:
        x+=1
        yield x

g=generador()

for x in range (1,100):
    print(next(g))"""


def mi_generador():
    x=1
    while True:
        x = x+7
        yield x


generador = mi_generador()

for x in range (1,100):
    print(next(generador))


def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()