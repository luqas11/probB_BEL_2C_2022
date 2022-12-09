# Cantidad de dígitos necesarios en una sucesión de dígitos decimales equiprobables para que la probabilidad de observar al menos un 6 sea mayor o igual a 0.99.

import time
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

i = 0
prob = 0
while True:
    prob = sps.binom.pmf(0, i, 1/10)
    if prob < 0.01:
        break
    i += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Cantidad de dígitos necesarios:", i)
print("Probabilidad de Yn > 0 = %.6f" % (1-prob))
