# Probabilidad de la cantidad de productos que están fallados y fueron detectados en una línea de producción con lotes de 6 productos, con probabilidad de falla de 1/4 y probabilidad de detección de fallas de 4/5.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 2000000
totals = np.zeros(7)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    partial = 0
    for j in range(0, 6):
        if np.random.rand() > 0.75:
            if np.random.rand() > 0.20:
                partial += 1
    totals[partial] += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad la cantidad de productos que están fallados y son detectados, de 0 a 6 respectivamente:", (totals / n))
