# Probabilidad de que una señal L se emita antes que una señal M, y a su vez ambas se emitan después de 30 segundos de comenzado el proceso.
# Las señales se emiten de acuerdo dos procesos puntuales de Poisson independientes de intensidades 3 y 5 por minuto, para las señales L y M respectivamente.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 3000000
total = 0
lambda_L = 1/3
lambda_M = 1/5

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    sl1 = np.random.exponential(scale = lambda_L)
    sm1 = np.random.exponential(scale = lambda_M)
    if sl1 > 0.5 and sm1 > 0.5 and sl1 < sm1:
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.5f" % (total / n))
