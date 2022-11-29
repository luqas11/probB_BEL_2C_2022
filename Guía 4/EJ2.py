# Función de probabilidad de la variable Y = |sen(X*pi/2)|, siendo X una variable aleatoria con distribución Poisson de media 2 (resolución parcial).

import time
import numpy as np
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

mu = 2

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

print ("{:<7} {:<7} {:<7}".format("x", "y", "px(x)"))
for i in range(0, 10):
    x = i
    y = np.abs(np.sin(0.5 * np.pi * x))
    print ("{:0.3f}   {:0.3f}   {:0.3f}".format(x, y, sps.poisson(mu).pmf(x)))

print()

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
