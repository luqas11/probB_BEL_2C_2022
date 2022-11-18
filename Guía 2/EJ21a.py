# Probabilidad de que la suma de la cantidad de bolas verdes o amarillas extraídas sin reposición de una urna con 3 bolas verdes, 2 amarillas y 3 rojas, sea menor que 3.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

extractions = 4
n = 1500000
# V - A - R
totals = [0, 0, 0]
sumLessThan3 = 0
test = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomBall(green_count, yellow_count, red_count):
    num = np.random.rand()
    if num >= (yellow_count + red_count)/(green_count + yellow_count + red_count):
        return green_count-1, yellow_count, red_count, 0
    elif num >= red_count/(green_count + yellow_count + red_count):
        return green_count, yellow_count-1, red_count, 1
    else:
        return green_count, yellow_count, red_count-1, 2

for i in range(0, n):
    partials = [0, 0, 0]
    green_count = 3
    yellow_count = 2
    red_count = 3
    result = 0
    for j in range(0, extractions):
        green_count, yellow_count, red_count, result = getRandomBall(green_count, yellow_count, red_count)
        partials[result] += 1
    if (partials[0] + partials[1]) <= 2:
        sumLessThan3 += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de que la suma de verdes y amarillas sea menor o igual a 2:\n%.3f" % (sumLessThan3 / n))
