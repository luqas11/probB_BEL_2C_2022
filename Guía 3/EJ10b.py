# Calcular la media del perímetro de un círculo cuyo área es una variable aleatoria con distribución exponencial de media 15.

import time
import numpy as np
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

def f(x):
    return np.sqrt(x*4*np.pi)

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

result = sps.expon(scale = 15).expect(f)

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Esperanza de g(X)=%.3f" % result)
