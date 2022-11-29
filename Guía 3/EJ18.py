# Probabilidad de que la cantidad de urnas con al menos una bola sea 1, 2, o 3 al colocar aleatoriamente 3 bolas en 3 urnas.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 1000000
totals = [0, 0, 0]

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomBallDistribution():
    return int(np.ceil(np.random.rand() * 3 - 1))

for i in range(0, n):
    partials = [0, 0, 0]
    count = 0
    for j in range(0, 3):
        partials[getRandomBallDistribution()] += 1
    for j in range(0, 3):
        if partials[j] != 0:
            count += 1
    totals[count-1] += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de que haya sólo 1 urna con al menos una bola: %.3f" % (totals[0] / n))
print("Probabilidad de que haya sólo 2 urnas con al menos una bola: %.3f" % (totals[1] / n))
print("Probabilidad de que las 3 urnas tengan al menos una bola: %.3f" % (totals[2] / n))
