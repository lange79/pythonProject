def suma(**kwargs):
    print(type(kwargs))

suma(x=3, y=5, z=2)


def suma(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

suma(x=3, y=5, z=2)

def suma(**kwargs):
    total=0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total+=valor
    return total

print(suma(x=3, y=5, z=2))



def prueba(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg= {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(15,50,100,200,300,400,x='uno',y='dos',z='tres',u=5)


args=[100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}
prueba(15,50,*args,**kwargs)


def describir_persona(nombre, **kwargs):
    print(f"Caracteristicas de {nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


describir_persona("María", color_ojos="azules", color_pelo="rubio")