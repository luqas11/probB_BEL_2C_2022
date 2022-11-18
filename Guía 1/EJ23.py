# Probabilidad de caminos abiertos o bloqueados, dado que la probabilidad de que un camino esté abierto es de 0.75 independientemente de los demás.
#      0   2
#     / \ / \
#    A   B   C
#     \ / \ /  
#      1   3
# Caminos: 0, 1, 2, 3
# Nodos: A, B, C

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 3000000
blockedAC = 0
openBC = 0
openBCandBlockedAC = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def isBlockedPath():
    return np.random.rand() >= 0.75

def blockedPaths():
    return [isBlockedPath(), isBlockedPath(), isBlockedPath(), isBlockedPath()]

for i in range(0, n):
    blocked = blockedPaths()
    if (blocked[0] and blocked[1]) or (blocked[2] and blocked[3]):
        blockedAC += 1
        if (not blocked[2] or not blocked[3]):
            openBCandBlockedAC += 1
    if (not blocked[2] or not blocked[3]):
        openBC += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de AC bloqueado: %.3f" % (blockedAC / n))
print("Probabilidad de BC abierto: %.3f" % (openBC / n))
print("Probabilidad de BC abierto y AC bloqueado: %.3f" % (openBCandBlockedAC / n))
print("Probabilidad de BC abierto dado AC bloqueado: %.3f" % (openBCandBlockedAC / blockedAC))
