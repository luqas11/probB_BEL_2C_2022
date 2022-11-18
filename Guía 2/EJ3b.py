# Probabilidad de que salgan n bolas verdes en 4 extracciones sin reposición de una urna de 3 bolas verdes y 5 rojas.

import time
import numpy as np

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

extractions = 4
n = 2000000
totals = [0, 0, 0, 0]

GREEN = "GREEN"
RED = "RED"

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def getRandomBall(red_count, green_count):
    if np.random.rand() >= green_count/(red_count + green_count):
        return red_count-1, green_count, RED
    else:
        return red_count, green_count-1, GREEN

for i in range(0, n):
    count = 0
    red_count = 5
    green_count = 3
    for j in range(0, extractions):
        red_count, green_count, ball_color = getRandomBall(red_count, green_count)
        if ball_color == GREEN:
            count += 1
        if green_count == 0:
            break
    totals[count] += 1


endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")
print("Probabilidad de que salgan 0, 1, 2 y 3 bolas verdes:\n%.3f\n%.3f\n%.3f\n%.3f" % (totals[0] / n, totals[1] / n, totals[2] / n, totals[3] / n))
