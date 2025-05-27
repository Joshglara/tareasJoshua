import numpy as np

# Red Neuronal
class redNeuronal:
    def __init__(self):
        # Pesos de las entradas
        self.pesos = np.array([0.5, 0.5, 0.5])  

    def forward(self, entradas):
        return np.dot(entradas, self.pesos)

# Ecuacion a evaluar
ecuacion = "2+3*10/9"

# Quita espacios
ecuacion = ecuacion.replace(" ", "")  

# Dividir los operandos y operadores de la ecuacion
operandos = []
operadores = []

operandoActual = ""
for char in ecuacion:
    if char.isdigit() or char == ".":
        operandoActual += char
    else:
        operandos.append(float(operandoActual))
        operandoActual = ""
        operadores.append(char)

# Añade ultimo operando
operandos.append(float(operandoActual))

# Crea arreglo de entradas
inputs = np.array(operandos[:-1])  # Excluye el ultimo operando (resultado)

# Evalua la ecuacion c/ la red
redNeuronal = redNeuronal()
output = redNeuronal.forward(inputs)

# Usa los operadores a la salida de manera secuencial
for operador, operando in zip(operadores, operandos[1:]):
    if operador == "+":
        output += operando
    elif operador == "-":
        output -= operando
    elif operador == "*":
        output *= operando
    elif operador == "/":
        output /= operando

# Resultado
print(f"Ecuacion: {ecuacion}")
print(f"Resultado: {output}")