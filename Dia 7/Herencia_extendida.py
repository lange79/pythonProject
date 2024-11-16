from symtable import Class


class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    """def __init__(self,edad,color,altura_vuelo):
        self.edad=edad
        self.color=color
        self.altura_vuelo=altura_vuelo"""

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

piolin= Pajaro(2, "amarillo", 40)
print(f"La edad de Piolin es: {piolin.edad}")
piolin.hablar()
piolin.volar(100)
mi_animal=Animal(2,"Negro")
print("El color de mi animal es:", mi_animal.color)


class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("Ja JA")
    def hablar(self):
        print("Que tal?")


class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.reir()
mi_nieto.hablar()
print(Nieto.__mro__)
