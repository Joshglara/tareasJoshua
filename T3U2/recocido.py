from datetime import datetime
import random, time, math
from copy import deepcopy, copy
import decimal

class Board:
    def __init__(self):
        #self.nReinas = int(input('Escoja la cantidad de reinas:'))
        self.nReinas = 8
        self.reseteo()

    def reseteo(self):
        self.reinas = [-1 for i in range(0, self.nReinas)]

        for i in range(0, self.nReinas):
            self.reinas[i] = random.randint(0, self.nReinas - 1)
        #self.reinas = [4, 1, 3, 5, 7 , 1, 6 , 2]

    def cuentaAtaques(self):
        ataques = 0
        
        for reina1 in range(0, self.nReinas):
            for reina2 in range(reina1 + 1, self.nReinas):
                if self.reinas[reina1] == self.reinas[reina2] or abs(reina1 - reina2) == abs(self.reinas[reina1] - self.reinas[reina2]):
                    ataques += 1
        return ataques

    def cuentaAtaquesReinas(reinas):
        ataques = 0
        nReinas = len(reinas)

        for reina in range(0, nReinas):
            for reina2 in range(reina+1, nReinas):
                if reinas[reina] == reinas[reina2] or abs(reina - reina2) == abs(reinas[reina] - reinas[reina2]):
                    ataques += 1

        return ataques

    def toString(reinas):
        board_string = ""

        for row, col in enumerate(reinas):
            if col + 1 == enumerate(reinas):
                board_string += "{}".format(col)
            else:
                board_string += "{}, ".format(col)

        return "[" + board_string[:-2] + "]"

    def vecinos(self):
        temp_reinas = self.reinas

        for i in range(0, self.nReinas):
            temp_reinas[i] = (temp_reinas[i] + 1) % (self.nReinas - 1)
            for j in range(i + 1, self.nReinas):
                temp_reinas[j] = (temp_reinas[j] + 1) % (self.nReinas - 1)

    def __str__(self):
        board_string = ""

        for row, col in enumerate(self.reinas):
            board_string += "({0}, {1})\n".format(row, col)

        return board_string

"""
--------------------- ALGORITMO ---------------------
"""

class Recocido:
    def __init__(self, board):
        self.tiempo = 0
        self.board = board
        self.temperatura = 4000
        self.degrado = 0.99
        self.startTime = datetime.now()


    def run(self):
        board = self.board
        boardReinas = self.board.reinas[:]
        solucion = False
        
        print("Tablero inicial:")
        print(Board.toString(self.board.reinas[:]))

        for k in range(0, 170000):
            self.temperatura = self.temperatura**(self.degrado)
            board.reseteo()
            vecino = board.reinas[:]
            dw = Board.cuentaAtaquesReinas(vecino) - Board.cuentaAtaquesReinas(boardReinas)
            # euler ^ (-ataquesTotales * temperatura)
            exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(self.temperatura)))
            
            if k % 17000 == 0:
                print('Procesando...')

            if dw > 0 or random.uniform(0, 1) < exp:
                boardReinas = vecino[:]

            if Board.cuentaAtaquesReinas(boardReinas) == 0:
                self.tiempo = self.getTiempo()
                print('\nPROBLEMA RESUELTO')
                
                print("Tiempo total: {} ms".format(str(self.tiempo)))
                print("Pasos: {}".format(k))
                print("Solucion:")
                print(Board.toString(boardReinas))
                solucion = True
                break

        if solucion == False:
            self.tiempo = self.getTiempo()
            print('\nPROBLEMA FALLIDO')
            print("Tiempo total: {} ms".format(str(self.tiempo)))
            print("Solucion:")
            print(Board.toString(boardReinas))
                

        return self.tiempo

    def getTiempo(self):
        tiempoSolucion = datetime.now()
        tiempo = (tiempoSolucion - self.startTime).microseconds / 1000
        return tiempo


if __name__ == '__main__':
    board = Board()
    Recocido(board).run()