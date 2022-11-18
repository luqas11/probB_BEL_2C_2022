# Probabilidad de Z < a dado que Z tiene distribución normal estándar.

import time
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

prob = 0
a = 0.9

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

prob = sps.norm.ppf(a)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad con: a=%.3f: %.5f" % (a, prob))
