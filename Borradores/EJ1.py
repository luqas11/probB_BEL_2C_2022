import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 200000
total = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    totals = [0, 0, 0]
    for j in range(0, 10):
        totals[np.random.randint(3)] += 1
    if totals[0] == 5 and (totals[1] == 3 or totals[2] == 3):
        total +=1
    if totals[1] == 5 and (totals[0] == 3 or totals[2] == 3):
        total +=1
    if totals[2] == 5 and (totals[0] == 3 or totals[1] == 3):
        total +=1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad: %.5f" % (total / n))
