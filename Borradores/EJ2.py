import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 100000
total = 0
h = 0.4418

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    sum = 0
    for j in range(0, 25):
        sum += np.random.uniform(5-h, 5+h)
    if np.abs(sum/25 - 5) > 0.1:
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.5f" % (total / n))
