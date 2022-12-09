# Probabilidad de que, en exactamente 10 minutos, se llene un estacionamiento que tiene 3 espacios vacíos, dado que cada minuto pasa un coche que tiene una probabilidad de estacionar de 0.8.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 700000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    partial = 0
    last_result = 0
    for j in range(0, 10):
        result = np.random.binomial(1, 0.8)
        partial += result
        last_result = result
    if partial == 3 and last_result == 1:
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.6f" % (total / n))
