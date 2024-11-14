class Pajaro:

    alas=True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color="Negro"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas= False
        print(Pajaro.alas)


    @staticmethod
    def mirar():
        print("El pajaro Mira!")



Pajaro.mirar()
Pajaro.poner_huevos(3)


piolin = Pajaro("Amarillo", "canario")
piolin.pintar_negro()
piolin.volar(50)
piolin.alas=False
print(piolin.alas)
