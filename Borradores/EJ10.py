import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

values = [41.1, 42.2, 40.5, 39.9, 40.3, 36.6, 39.3, 42.5, 37.8, 40.5]
Q = 0
S_2 = 0
prom = 0
mu = 40

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

prom = np.mean(values)

for i in range(0, len(values)):
    S_2 += (values[i] - prom)**2
S_2 = S_2 / (len(values) - 1)

Q = (prom - mu) / (np.sqrt(S_2) / np.sqrt(len(values)))

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Valor de Q:", Q)
