# Probabilidad de Z < a dado que Z tiene distribución normal estándar y a es igual a 0.5, 0.75, 0.9, 0.99, 0.995 o 0.999.

import time
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

a = [0.5, 0.75, 0.9, 0.99, 0.995, 0.999]

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(0, len(a)):
    print("Probabilidad con a=%.3f: %.5f" % (a[i], sps.norm.ppf(a[i])))

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
