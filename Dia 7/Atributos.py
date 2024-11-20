class Pajaro:

    alas=True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro=Pajaro("negro", "Tucan")

palabra = "Hola"

print(f" Mi pajaro es un {mi_pajaro.especie} y es del color {mi_pajaro.color}")
print(Pajaro.alas)
print((mi_pajaro.alas))


"""
lass Pajaro:

    def __init__(self, mi_parametro):
        self.mi_atributo = mi_parametro


mi_pajaro=Pajaro("negro")

palabra = "Hola"

print(mi_pajaro.mi_atributo)"""


class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa ("Blanco",4)

print(casa_blanca)

class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje("Humano", "True", 17)
