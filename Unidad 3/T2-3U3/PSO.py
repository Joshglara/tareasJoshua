import numpy as np

#Funcion a optimizar
def funcionObjetivo(x):
    return np.sum(x**2)

#Clase Particula
class Particula:
    def __init__(self, limite):
        self.posicion = np.random.uniform(limite[:, 0], limite[:, 1])
        self.velocidad = np.zeros_like(self.posicion)
        self.maxLocal = self.posicion.copy()
        self.maxValor = float('inf')
        
    def calcVelocidad(self, optimoGlobal, inercia=0.5, cognitiva=1.5, social=1.5):
        r1, r2 = np.random.rand(2)
        velCognitiva = cognitiva * r1 * (self.maxLocal - self.posicion)
        velSocial = social * r2 * (optimoGlobal - self.posicion)
        self.velocidad = inercia * self.velocidad + velCognitiva + velSocial

    def moverParticula(self, limite):
        self.posicion += self.velocidad
        self.posicion = np.clip(self.posicion, limite[:, 0], limite[:, 1])
        valor = funcionObjetivo(self.posicion)
        if valor < self.maxValor:
            self.maxValor = valor
            self.maxLocal = self.posicion.copy()

def crearEnjambre(num,limite):
    enjambre = []
    for i in range(num):
        enjambre.append(Particula(limite))
    return enjambre

def moverEnjambre(enjambre, limite)
    for particula in enjambre:
            particula.moverParticula(limite)
            if particula.maxValor < maxGlobalValor:
                maxGlobalValor = particula.maxValor
                maxGlobal = particula.maxLocal
                
    for particula in enjambre:
        particula.calcVelocidad(maxGlobal)
    return maxGlobal, maxGlobalValor


#Algoritmo enjambre de particulas
def PSO(numParticulas, limite):
    limite = np.array(limite)
    maxIter=100
    enjambre = crearEnjambre(numParticulas,limite)
    maxGlobal = None
    maxGlobalValor = float('inf')

    for i in range(maxIter):
        maxGlobal, maxGlobalValor = moverEnjambre(enjambre,limite)
    return maxGlobal, maxGlobalValor

#Codigo a ejecutar
limite = [(-5, 5), (-5, 5)]
maxGlobal, maxGlobalValor = PSO(30, limite)
print(f"Maximo global: {maxGlobalValor}")
print(f"Posicion: {maxGlobal}")
