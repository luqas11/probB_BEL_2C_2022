# Probabilidad de que se haya utilizado una moneda equilibrada al lanzar una de entre tres monedas, dos equilibradas y una de dos caras, siendo que se obtuvo una cara.
# Ai = el lanzamiento i es cara.
# C = la moneda elegida para los lanzamientos tiene dos caras

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 6000000
resultA1 = 0
resultNotCandA1 = 0

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
        if coin == BALANCED:
            resultNotCandA1 += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de A1: %.3f" % (resultA1 / n))
print("Probabilidad de noC y A1: %.3f" % (resultNotCandA1 / n))
print("Probabilidad de noC dado A1: %.3f" % (resultNotCandA1 / resultA1))
