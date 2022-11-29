# Esperanza de una variable aleatoria con distribución Poisson de media 3 condicionada a ser menor o igual a 2.

import time
import scipy.stats as sps

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

result = sps.expon(scale = 3).expect(lb=0, ub=2, conditional = True)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================
# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Esperanza de g(X)=%.3f" % result)
