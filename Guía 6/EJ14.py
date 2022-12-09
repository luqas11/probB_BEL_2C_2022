# Probabilidad de que, en una variable aleatoria con distribución multinomial M(9, 1/2, 1/3, 1/6), la variable X2 sea igual a 3.

import time
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

result = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, 7):
    rv = sps.multinomial(9, [1/2, 1/3, 1/6])
    result += rv.pmf([i, 3, 6-i])

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.6f" % result)
