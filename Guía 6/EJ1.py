# Probabilidad de que un paquete de piezas no satisfaga la garantía del fabricante de que como máximo hay 1 pieza defectuosa en un paquete de 10.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 1000000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def isDefectivePiece():
    return np.random.rand() > 0.01

for i in range(0, n):
    count = 0
    for j in range(0, 10):
        if not isDefectivePiece():
            count += 1
        if count == 2:
            total += 1
            break

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.3f" % (total / n))
