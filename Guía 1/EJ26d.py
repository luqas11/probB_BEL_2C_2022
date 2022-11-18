# Probabilidad de que se haya utilizado una moneda equilibrada al lanzar tres veces una de entre tres monedas, dos equilibradas y una de dos caras, siendo que se obtuvieron tres caras.
# Ai = el lanzamiento i es cara.
# C = la moneda elegida para los lanzamientos tiene dos caras

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================
n = 4000000
resultA3andA2andA1 = 0
resultNotCandA3andA2andA1 = 0

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
        result, coin = getCoinRandomResult(coin)
        if result:
            result, coin = getCoinRandomResult(coin)
            if result:
                resultA3andA2andA1 += 1
                if coin == BALANCED:
                    resultNotCandA3andA2andA1 += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================
# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de A1, A2 y A3: %.3f" % (resultA3andA2andA1 / n))
print("Probabilidad de noC dado A1, A2 y A3: %.3f" % (resultNotCandA3andA2andA1 / resultA3andA2andA1))
