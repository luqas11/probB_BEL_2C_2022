# Probabilidad de que la cantidad de marcas en un proceso puntual de Poisson de intensidad 2 hasta el tiempo 1 sea cero.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 7000000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    if(np.random.exponential(scale = 0.5) > 1):
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.5f" % (total / n))
