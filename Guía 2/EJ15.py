# Gráfico de la función de distribución empírica de una VA de distribución uniforme transformada por la función h(t).
# h(t) = -2 * 1{0 <= t < 1/3} + 6t - 3 * 1{1/3 <= t < 2/3} + 2 * 1{2/3 <= t < 1}

import time
import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

n = 10000
data = []
PLOT_POINTS = 1000

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def h(t):
    if (0 <= t < 1/3):
        return -2
    if (1/3 <= t < 2/3):
        return 6*t - 3
    if (2/3 <= t < 1):
        return 2

for i in range (0, n):
    data.append(h(np.random.rand()))

sorted_data = sorted(data)

def fde(t):
    counter = 0
    for i in range(0, len(sorted_data)):
        if (sorted_data[i] <= t):
            counter += 1
        else:
            break
    return counter / len(sorted_data)

margin = (sorted_data[len(sorted_data)-1] - sorted_data[0]) * 0.1
x = np.linspace(sorted_data[0] - margin, sorted_data[len(sorted_data)-1] + margin, PLOT_POINTS)
y = np.array(list(map(fde, x)))

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")

plt.plot(x, y, 'ro')
plt.title('Función de distribución empírica')
plt.grid(True)

plt.show()
