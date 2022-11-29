# Probabilidad de que la variable aleatoria Z1 se encuentre entre 0 y 1, siendo Z1 una variable con distribución Z1 = R*cos(theta), con:
# U1 y U1 variables aleatorias independientes con distribución uniforme entre 0 y 1.
# R = sqrt(-2*log(U1))
# theta = 2*pi*U2

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================
n = 1500000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    u1 = np.random.rand()
    u2 = np.random.rand()
    r = np.sqrt(-2 * np.log(u1))
    theta = 2 * np.pi * u2
    z1 = r * np.cos(theta)
    if z1 > 0 and z1 < 1:
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.3f" % (total / n))
