# Calcular la media del área de un círculo cuyo perímetro es una variable aleatoria con distribución exponencial de media 60.

import time
import numpy as np
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

def f(x):
    return x**2/(4*np.pi)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

result = sps.expon(scale = 60).expect(f)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Esperanza de g(X)=%.3f" % result)
