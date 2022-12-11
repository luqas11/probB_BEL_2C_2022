import time
import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================
n = 100000
count = 100
totals = np.zeros(count + 1, dtype = float)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, n):
    counter = 0
    for j in range(0, count):
        if np.random.rand() < 0.5:
            counter += 1
    totals[counter] += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")

fig, ax = plt.subplots()
ax.bar(range(0, count + 1), totals / n, width = count / 100, edgecolor="white")
plt.show()
