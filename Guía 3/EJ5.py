# Esperanza de una variable aleatoria con distribución Poisson de media 10 condicionada a ser menor o igual a 4.

import time
import scipy.stats as sps

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

result = sps.poisson(10).expect(lb=0, ub=4, conditional = True)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Esperanza de g(X)=%.3f" % result)
