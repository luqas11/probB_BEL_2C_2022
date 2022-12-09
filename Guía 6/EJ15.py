# Probabilidad de que haya menos de 5 piezas defectuosas en un lote de 8, siendo que pueden tener un defecto de tipo A con probabilidad 0.1 y un defecto de tipo B con probabilidad 0.2.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 700000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    partials = [0, 0, 0]
    for j in range(0, 8):
        a = np.random.rand() < 0.1
        b = np.random.rand() < 0.2
        if a and b:
            partials[2] += 1
        elif a:
            partials[0] += 1
        elif b:
            partials[1] += 1
    if (partials[0] + partials[1] + partials[2]) < 5:
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.6f" % (total/n))
