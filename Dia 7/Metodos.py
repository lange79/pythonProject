class Pajaro:

    alas=True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(50)


class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


alarma = Alarma()
alarma.postergar(50)