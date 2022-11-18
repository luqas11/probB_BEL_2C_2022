# Probabilidad de que al arrojar dos dados su suma sea menor a 11.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 2000000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomDiceNumber():
    return np.ceil(np.random.rand() * 6)

for i in range(0, n):
    sum = getRandomDiceNumber() + getRandomDiceNumber()
    if (sum < 11):
        total += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.3f" % (total / n))
