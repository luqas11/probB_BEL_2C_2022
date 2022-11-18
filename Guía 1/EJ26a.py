# Probabilidad de obtener cara por segunda vez al lanzar dos veces una de entre tres monedas, dos equilibradas y una de dos caras, siendo que ya se obtuvo una cara.
# Ai = el lanzamiento i es cara.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 5000000
resultA1 = 0
resultA2andA1 = 0

NONE = 0
BALANCED = "BALANCED"
UNBALANCED = "UNBALANCED"

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getCoinRandomResult(coin):
    if coin == BALANCED:
        return np.random.rand() >= 1/2, BALANCED
    if coin == UNBALANCED:
        return True, UNBALANCED
    if coin == NONE:
        if np.random.rand() >= 1/3:
            return np.random.rand() >= 1/2, BALANCED
        else:
            return True, UNBALANCED

for i in range(0, n):
    result, coin = getCoinRandomResult(NONE)
    if result:
        resultA1 += 1
        result, coin = getCoinRandomResult(coin)
        if result:
            resultA2andA1 += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de A1: %.3f" % (resultA1 / n))
print("Probabilidad de A2 y A1: %.3f" % (resultA2andA1 / n))
print("Probabilidad de A2 dado A1: %.3f" % (resultA2andA1 / resultA1))
