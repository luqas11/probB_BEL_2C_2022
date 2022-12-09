# Probabilidad de que, en un proceso puntual de Poisson de intensidad 2, la tercer marca ocurra después del tiempo 1/2, sabiendo que hasta el tiempo 1/4 ocurrió exactamente 1 marca.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 2000000
total = 0
_total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    s1 = np.random.exponential(scale = 0.5)
    s2 = s1 + np.random.exponential(scale = 0.5)
    s3 = s2 + np.random.exponential(scale = 0.5)
    if s1 < 0.25 and s2 > 0.25:
        if s3 > 0.5:
            total += 1
        _total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.5f" % (total / _total))
