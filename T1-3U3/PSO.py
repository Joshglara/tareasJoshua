import numpy as np

class Particula:
    def __init__(self, limite):
        self.posicion = np.random.uniform(limite[:, 0], limite[:, 1])
        self.velocidad = np.zeros_like(self.posicion)
        self.maxLocal = self.position.copy()
        self.maxGlobal = float('inf')
		
def crearParticula(num, limite):
    enjambre = []
		for i in range num:
			enjambre.append(Particula(limite))
	return enjambre

limite = np.array([(-5, 5), (-5, 5)])
enjambre = crearParticula(5,limite)