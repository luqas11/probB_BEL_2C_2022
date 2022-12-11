import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 5000000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomCount():
    num = np.random.rand()
    if num >= 0.6:
        return 0
    elif num >= 0.25:
        return 1
    else:
        return 2


for i in range(0, n):
    client1 = getRandomCount()
    client2 = getRandomCount()
    if client1 == 1 and client2 == 0:
        total += 1
    if client1 == 0 and client2 == 1:
        total += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad:\n%.3f" % (total / n))
