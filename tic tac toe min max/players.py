import math
import random

class jugador:
    def __init__(self, letra):
        self.letra = letra

    def mueve(self, juego):
        pass

class computadora_aleatorio(jugador):
    def __init__(self, letra):
        super().__init__(letra)

    def mueve(self, juego):
        cuadro = random.choice(juego.cuadros_vacios())
        return cuadro

class los_pibes(jugador):
    def __init__(self, letra):
        super().__init__(letra)

    def mueve(self, juego):
        cuadro_libre = False
        numero = None
        while not cuadro_libre:
            cuadro = input(self.letra + "es tu turno de elegir un cuadro del (0 al 9)")
            try:
                numero = int(cuadro)
                if numero not in juego.cuadros_vacios():
                    raise ValueError
                cuadro_libre = True
            except ValueError:
                print("valor incorrecto intentalo de nuevo")

        return numero