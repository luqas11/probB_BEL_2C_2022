# Valor c que minimiza el error de un receptor de señales que procesa la señal recibida únicamente cuando es mayor a un valor c.
# La señal se emite con una amplitud aleatoria X = S + N, donde S es una variable Bernoulli de parámetro 3/4 y N es un ruido con distribución normal N(0, 1/2).
# La señal sólo contiene información útil cuando S = 1. El receptor comete un error cuando procesa una señal con S = 0, o cuando no procesa una señal con S = 1.

import time
import numpy as np
import scipy.stats as sps

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 30000
min_c = 0
min_prob = np.inf

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

for i in range(1, n):
    c = i*2/n - 1
    error_prob = 1/4 * sps.norm.cdf(-2*c) + 3/4 * sps.norm.cdf(2*c - 2)
    if (error_prob < min_prob):
        min_prob = error_prob
        min_c = c

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("El valor de c que minimiza el error es %.5f, con una probabilidad de error de %.5f" % (min_c, min_prob))
