# Probabilidad de que la tercer marca en un proceso puntual de Poisson de intensidad 2 ocurra después del tiempo 1/2.

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

for i in range(0, n):
    s3 = np.random.exponential(scale = 0.5) + np.random.exponential(scale = 0.5) + np.random.exponential(scale = 0.5)
    if(s3 > 0.5):
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.5f" % (total / n))
