# Probabilidad de que la variable aleatoria Z2/Z1 sea menor a sqrt(3), siendo Z1 y Z1 variables con distribución normal estándar.

import time
import numpy as np
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================
n = 100000
counter = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    z1 = sps.norm.rvs()
    z2 = sps.norm.rvs()
    if z2/z1 < np.sqrt(3):
        counter += 1
endTime = time.perf_counter_ns()

# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.3f" % (counter / n))
