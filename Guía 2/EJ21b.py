# Probabilidad de que la suma de la cantidad de bolas verdes o amarillas extraídas con reposición de una urna con 3 bolas verdes, 2 amarillas y 3 rojas, sea menor que 3.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================
extractions = 4
n = 2000000
# V - A - R
totals = [0, 0, 0]
sumLessThan3 = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomBall():
    num = np.random.rand()
    if num >= 5/8:
        return 0
    elif num >= 3/8:
        return 1
    else:
        return 2


for i in range(0, n):
    partials = [0, 0, 0]
    for j in range(0, extractions):
        partials[getRandomBall()] += 1
    if (partials[0] + partials[1]) <= 2:
        sumLessThan3 += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================
# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de que la suma de verdes y amarillas sea menor o igual a 2:\n%.3f" % (sumLessThan3 / n))
