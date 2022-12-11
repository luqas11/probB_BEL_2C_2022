import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

extractions = 7
n = 1000000
has2or3or4red = 0

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomCard(green_count, red_count):
    num = np.random.rand()
    if num >= (red_count)/(green_count + red_count):
        return green_count-1, red_count, 0
    else:
        return green_count, red_count-1, 1

for i in range(0, n):
    partials = [0, 0]
    green_count = 36
    red_count = 24
    result = 0
    for j in range(0, extractions):
        green_count, red_count, result = getRandomCard(green_count, red_count)
        partials[result] += 1
    if partials[1] == 2 or partials[1] == 3 or partials[1] == 4:
        has2or3or4red += 1

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad:\n%.3f" % (has2or3or4red / n))
