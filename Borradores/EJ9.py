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

def getRandomCount():
    num = np.random.rand()
    if num >= 2/3:
        return 0
    elif num >= 1/6:
        return 1
    else:
        return 2


for i in range(0, n):
    partials = [0, 0, 0]
    for j in range(0,4):
        partials[getRandomCount()] += 1
    if partials[1] == 3 and partials[2] == 1:
        total += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad:\n%.5f" % (total / n))
