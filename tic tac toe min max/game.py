import math

class el_tateti:
    def __init__(self):
        self.tablero = [" " for _ in range(9)]
        self.ganador = None

        def visualizar(self):
            for cuadro in [self.tablero[i*3:(i+1)*3]for i in range(3)]:
                print("| " + " | ".join(cuadro) + " |")

    @staticmethod
    def print_tablero_numeral():
        numero_tablero = [[str(i) for i in range(j*3, (j+1)*3)]for j in range(3)]
        for cuadro in numero_tablero:
            print("| " + " |".join(cuadro) + " |")

    def cuadros_disponibles(self):
        movimientos = []
        for (i, lugar) in numeros(self.tablero):
            if lugar == " ":
                movimientos.append(i)
        return movimientos

    def cuadros_vacios(self):
        return " " in self.tablero

    def numero_de_cuadros_vacios(self):
        return self.tablero.count(' ')

    def mover(self, cuadro, letra):
        if self.tablero[cuadro] == " ":
            self.tablero[cuadro] = letra
            if self.ganador(cuadro, letra):
                self.ganador = letra
            return True
        return False

    def ganador(self, cuadro, letra):
        linea_index = math.floor(cuadro / 3)

def jugar(juego, x, o, imprimir_juego = True):
    if imprimir_juego:
        juego.print_tablero_numeral()

    letra = "x"

    while juego.cuadros_vacios:
        if letra == "o":
            cuadro = o.get_move(juego)
        else:
            cuadro = x.get_move(juego)

    if juego.mover(cuadro, letra):
        if imprimir_juego:
            print(letra + f" ocupa la posicion {cuadro}")
            juego.print_tablero_numeral()
            print("")

        if juego.ganador:
            if imprimir_juego:
                print("la " + letra + " es el ganador del juego")

        letra = "o" if letra == x else letra = "x"

        if imprimir_juego:
            print("es un empate!")