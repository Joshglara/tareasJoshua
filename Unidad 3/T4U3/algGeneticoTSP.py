import random
import math
import matplotlib.pyplot as plt


# Posicion de las ciudades
def getCiudad():
    ciudades = [
        [1, 80, 260],
        [2, 115, 350],
        [3, 210, 85],
        [4, 290, 150],
        [5, 310, 275],
        [6, 405, 205],
        [7, 410, 460],
        [8, 580, 40],
        [9, 585, 180],
        [10, 610, 360],
        [11, 750, 120],
        [12, 830, 225],
        [13, 885, 330],
        [14, 970, 405],
    ]
    return ciudades


# Calcular distancia entre ciudades
def calcDistancia(ciudades):
    sumaTotal = 0
    for i in range(len(ciudades) - 1):
        ciudadA = ciudades[i]
        ciudadB = ciudades[i + 1]

        d = math.sqrt(
            math.pow(ciudadB[1] - ciudadA[1], 2) + math.pow(ciudadB[2] - ciudadA[2], 2)
        )

        sumaTotal += d

    ciudadA = ciudades[0]
    ciudadB = ciudades[-1]
    d = math.sqrt(math.pow(ciudadB[1] - ciudadA[1], 2) + math.pow(ciudadB[2] - ciudadA[2], 2))

    sumaTotal += d

    return sumaTotal


# Selecciona la poblacion
def selecPoblacion(ciudades, tam):
    poblacion = []

    for i in range(tam):
        c = ciudades.copy()
        random.shuffle(c)
        distancia = calcDistancia(c)
        poblacion.append([distancia, c])
    aptitud = sorted(poblacion)[0]

    return poblacion, aptitud


# Algoritmo
def algoritmoGenetico(poblacion, lenCiudades, torneoTamSelec,
                        tasaMutacion, tasaCrossover, meta,):
    gen_numero = 0
    for i in range(200):
        poblacionNueva = []

        # Escoger los mejores dos cromosomas
        poblacionNueva.append(sorted(poblacion)[0])
        poblacionNueva.append(sorted(poblacion)[1])

        for i in range(int((len(poblacion) - 2) / 2)):
            # CROSSOVER
            numRandom = random.random()
            if numRandom < tasaCrossover:
                cromPadre1 = sorted(
                    random.choices(poblacion, k=torneoTamSelec)
                )[0]

                cromPadre2 = sorted(
                    random.choices(poblacion, k=torneoTamSelec)
                )[0]

                point = random.randint(0, lenCiudades - 1)

                cromHijo1 = cromPadre1[1][0:point]
                for j in cromPadre2[1]:
                    if (j in cromHijo1) == False:
                        cromHijo1.append(j)

                cromHijo2 = cromPadre2[1][0:point]
                for j in cromPadre1[1]:
                    if (j in cromHijo2) == False:
                        cromHijo2.append(j)

            # Si no ocurre crossover
            else:
                cromHijo1 = random.choices(poblacion)[0][1]
                cromHijo2 = random.choices(poblacion)[0][1]

            # Mutacion
            if random.random() < tasaMutacion:
                point1 = random.randint(0, lenCiudades - 1)
                point2 = random.randint(0, lenCiudades - 1)
                cromHijo1[point1], cromHijo1[point2] = (
                    cromHijo1[point2],
                    cromHijo1[point1],
                )

                point1 = random.randint(0, lenCiudades - 1)
                point2 = random.randint(0, lenCiudades - 1)
                cromHijo2[point1], cromHijo2[point2] = (
                    cromHijo2[point2],
                    cromHijo2[point1],
                )

            poblacionNueva.append([calcDistancia(cromHijo1), cromHijo1])
            poblacionNueva.append([calcDistancia(cromHijo2), cromHijo2])

        poblacion = poblacionNueva

        gen_numero += 1

        if gen_numero % 10 == 0:
            print(gen_numero, sorted(poblacion)[0][0])

        if sorted(poblacion)[0][0] < meta:
            break

    solucion = sorted(poblacion)[0]

    return solucion, gen_numero


# dibuja ciudades y mapa
def dibujaMapa(ciudad, solucion):
    for j in ciudad:
        plt.plot(j[1], j[2], "ro")
        plt.annotate('%.1f \n(%.1f, %.1f)'%(j[0],int(j[1]),int(j[2])), (j[1], j[2]))

    for i in range(len(solucion[1])):
        try:
            first = solucion[1][i]
            second = solucion[1][i + 1]

            plt.plot([first[1], second[1]], [first[2], second[2]], "gray")
        except:
            continue

    first = solucion[1][0]
    second = solucion[1][-1]
    plt.plot([first[1], second[1]], [first[2], second[2]], "gray")

    plt.show()


def main():
    # Valores iniciales
    poblacion = 200
    torneoTamSelec = 4
    tasaMutacion = 0.2
    tasaCrossover = 0.9
    meta = 2500.0

    ciudades = getCiudad()
    primeraPoblacion, primerosAptos = selecPoblacion(ciudades, poblacion)
    solucion, numGen = algoritmoGenetico(
        primeraPoblacion,
        len(ciudades),
        torneoTamSelec,
        tasaMutacion,
        tasaCrossover,
        meta,
    )

    print("\n----------------------------------------------------------------")
    print("Generacion: " + str(numGen))
    print("Cromosoma mas apto antes del torneo: " + str(primerosAptos[0]))
    print("Cromosoma mas apto despues del torneo: " + str(solucion[0]))
    print("Distancia meta: " + str(meta))
    print("----------------------------------------------------------------\n")

    dibujaMapa(ciudades, solucion)


main()
