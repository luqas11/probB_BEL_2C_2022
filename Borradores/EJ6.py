import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 300000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    partial = 0
    cards = np.random.choice(60, 7, replace=False)
    for i in range(0, len(cards)):
        if cards[i] < 24:
            partial += 1
    if partial == 2 or partial == 3 or partial == 4:
        total += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad:\n%.3f" % (total / n))
