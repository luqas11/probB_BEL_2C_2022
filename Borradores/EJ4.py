import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 50000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def isRedBall():
    if np.random.rand() >= 13/28:
        return False
    else:
        return True


for i in range(0, n):
    count = 0
    for j in range(0, 200):
        if isRedBall():
            count += 1
        if count > 90:
            total += 1
            break


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad:\n%.3f" % (total / n))
