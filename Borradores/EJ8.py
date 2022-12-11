import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 1000000
total = 0
_total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    prov = np.random.rand() > 1/3
    failure = 0
    if prov:
        failure = 8/100
    else:
        failure = 10/100

    partial = 0
    for j in range(0, 15):
        if np.random.rand() < failure:
            partial += 1
    if partial == 2:
        _total += 1
        if prov:
            total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad:\n%.5f" % (total / _total))
