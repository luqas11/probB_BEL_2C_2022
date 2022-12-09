# Esperanza de la cantidad de 3 observados en un dado equilibrado que se lanza una vez cada 20 segundos, durante un período de tiempo dado por una variable aleatoria con distribución exponencial de media 3hs.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 2000000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    total_time = np.random.exponential(scale=3)
    dice_rolls = np.ceil((total_time * 3600/20))
    total += np.random.binomial(dice_rolls, 1/6)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Esperanza: %.3f" % (total / n))
