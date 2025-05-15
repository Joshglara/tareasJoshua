from datetime import datetime
import random
import numpy as np

reinasMax = 15
iteracionesMax = 100
listaTabuTam = 10


def puedenAtacar(colum1, fila1, colum2, fila2):
    """
    Checa si 2 posiciones se pueden atacar.
    True si las reinas pueden atacarse, False sino.
    """
    if colum1 == colum2:
        return True  # Misma columna
    if fila1 == fila2:
        return True  # Misma fila
    if abs(colum1 - colum2) == abs(fila1 - fila2):
        return True  # Diagonal

    return False


def atacaOtraReina(fila1, colum1, board):
    """
    Checa si en la posición dada hay una reina que pueda atacar a otra.
    True si la reina puede atacar, False sino.
    """
    for colum2, fila2 in enumerate(board):
        if puedenAtacar(colum1, fila1, colum2, fila2):
            if fila1 != fila2 or colum1 != colum2:
                return True
    return False


def cuentaAtaques(board):
    """
    Cuenta el numero de reinas atacandose.
    """
    cant = 0

    for reina1 in range(0, len(board)):
        for reina2 in range(reina1 + 1, len(board)):
            if puedenAtacar(reina1, board[reina1], reina2, board[reina2]):
                cant += 1

    return cant

def vecinos(board):

    """
    Genera soluciones vecinas a la solucion entrada.
    """

    vecinos = []
    
    """
    for _ in range(len(board)):
        rand_col = random.sample(range(len(board)), len(board))
        vecino = board[:]
        for col in rand_col:
            vecino[col] = random.randint(0, len(board) - 1)
        vecinos.append(vecino)
    """
    
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            vecino = board[:]
            vecino[i], vecino[j] = vecino[j], vecino[i]
            vecinos.append(vecino)
    
    return vecinos
    
"""
def evalua(board):
    
    Calcula el valor de un tablero. El maximo de ataques en un tablero N es ((N-1) * N)/2.
    Como funciona por busqueda ascendente, la funcion da (((N-1) * N) / 2) - cuentaAtaques(board)
    
    return (len(board) - 1) * len(board) / 2 - cuentaAtaques(board)
"""

def print_board(board):
    """
    Imprime el tablero en un formato legible con las reinas. Q mayuscula para aquellas
    que se puedan atacar, minuscula para las que no.
    """
    for row in range(len(board)):
        line = ''
        for column in range(len(board)):
            if board[column] == row:
                line += 'Q' if atacaOtraReina(row, column, board) else 'q'
            else:
                line += '-'
        print(line)
    print("")


def init_board(nReinas):
    """
    Genera la solucion origen
    """
    board = []
    """
    for column in range(nReinas):
        board.append(random.randint(0, nReinas - 1))
    """
    board = random.sample(range(nReinas), nReinas)
    return board


"""
--------------------- ALGORITMO ---------------------
"""


def busquedaTabu(board, iteracionesMax, listaTabuTam):
    inicio = datetime.now()
    mejorSolucion = board
    solucionActual = board
    listaTabu = []
    mejorVecino = None
    mejorVecinoAtaques = float('inf')
    i = 0
    
    while cuentaAtaques(solucionActual) != 0:
        print("Lista tabu: ",listaTabu)
        listaVecinos = []
        i += 1
        
        listaVecinos = vecinos(solucionActual)
        
        if i == iteracionesMax:  # Give up after MAX_ITER tries.
            break
        
        for vecino in listaVecinos:
            if vecino not in listaTabu:
                vecinoAtaques = cuentaAtaques(vecino)
                if vecinoAtaques <= mejorVecinoAtaques:
                    mejorVecino = vecino
                    mejorVecinoAtaques = vecinoAtaques

        if mejorVecino is None:
            break

        listaTabu.append(solucionActual)
        solucionActual = mejorVecino
        
        if len(listaTabu) > listaTabuTam: 
            # Elimina registro mas antiguo si supera el tamaño de la lista
            listaTabu.pop(0)

        if cuentaAtaques(mejorVecino) < cuentaAtaques(mejorSolucion):
            # Actualiza la mejor solucion si el vecino es mejor
            mejorSolucion = mejorVecino
            
        print(f"Recursión {i}: Ataques = {cuentaAtaques(solucionActual)}")
        print(solucionActual)
        print_board(solucionActual)

    if cuentaAtaques(mejorSolucion) == 0:
        print('\nPROBLEMA RESUELTO')

    print('Solucion:')
    print(mejorVecino)
    print_board(mejorVecino)
    print("Tiempo total: {} ms".format(str((datetime.now()-inicio).microseconds/1000)))

def main():
    nReinas = int(input('Escoja la cantidad de reinas:'))
    
    try:
        if nReinas < 4 or nReinas > reinasMax:
            raise ValueError

    except ValueError:
        print('Valor invalido!!!')
        return False

    board = init_board(nReinas)
    print('\nTablero inicial:')
    print(board)
    print_board(board)

    busquedaTabu(board, iteracionesMax, listaTabuTam)
    #Optimized_Hill_Climbing(board)

if __name__ == "__main__":
    main()
