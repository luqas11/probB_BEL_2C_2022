# Probabilidad de obtener al menos un uno en 6 tiros de dado.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 1000000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomDiceNumber():
    return np.ceil(np.random.rand() * 6)

for i in range(0, n):
    for j in range(0, 6):
        if getRandomDiceNumber() == 1:
            total += 1
            break


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.3f" % (total / n))
