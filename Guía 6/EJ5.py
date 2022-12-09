# Cantidad de lanzamientos necesarios de un dado equilibrado para que, con probabilidad mayor o igual a 0.95, la frecuencia relativa con la que sale un 5 sea de 1/6 +- 0.01.

import time
import numpy as np
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

i = 1
min = 0
max = 0
prob = 0
while(True):
    min = int(np.ceil(47*i/300) - 1)
    max = int(np.floor(53*i/300))
    prob = sps.binom.cdf(max, i, 1/6) - sps.binom.cdf(min, i, 1/6)
    if(prob >= 0.95):
        break
    i += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Cantidad de lanzamientos necesarios:", i)
print("Probabilidad: %.5f" % prob)
