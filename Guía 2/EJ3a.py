# Probabilidad de que salgan n bolas verdes en 4 extracciones con reposición de una urna de 3 bolas verdes y 5 rojas.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

extractions = 4
n = 2000000
totals = [0, 0, 0, 0, 0]

GREEN = "GREEN"
RED = "RED"

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomBall():
    if np.random.rand() >= 3/8:
        return RED
    else:
        return GREEN

for i in range(0, n):
    count = 0
    for j in range(0, extractions):
        if getRandomBall() == GREEN:
            count += 1
    totals[count] += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de que salgan 0, 1, 2, 3, y 4 bolas verdes:\n%.3f\n%.3f\n%.3f\n%.3f\n%.4f" % (totals[0] / n, totals[1] / n, totals[2] / n, totals[3] / n, totals[4] / n))
