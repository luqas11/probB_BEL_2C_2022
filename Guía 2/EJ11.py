# Gráfico de la función empírica para los valores 8.59, 8.77, 8.29, 7.50, 9.18, 8.53, 10.03, 8.97, 8.47, 9.98, 9.00, 9.44, 8.02, 10.35, 7.15, 9.00, 9.15, 9.11, 7.63, 9.66, 10.20, 9.01, 8.73 y 10.54.
# Gráfico de la función histograma para los valores mencionados tomando como límites de los intervalos a 7.1, 7.85, 8.35, 9.65, 10.15 y 10.90.

import time
import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

data = [ 8.59, 8.77, 8.29, 7.50, 9.18, 8.53, 10.03, 8.97, 8.47, 9.98, 9.00, 9.44, 8.02, 10.35, 7.15, 9.00, 9.15, 9.11, 7.63, 9.66, 10.20, 9.01, 8.73, 10.54]
sorted_data = sorted(data)
bin_limits = [ 7.1, 7.85, 8.35, 9.65, 10.15, 10.90]
PLOT_POINTS = 10000

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

def fde(t):
    counter = 0
    for i in range(0, len(sorted_data)):
        if (sorted_data[i] <= t):
            counter += 1
        else:
            break
    return counter / len(sorted_data)

def hist(t):
    counter = 0
    bin_limit_inf = 0
    bin_limit_sup = 0
    if (t < bin_limits[0]) or t > (bin_limits[len(bin_limits)-1]):
        return counter
    for i in range(0, len(bin_limits)):
        if (bin_limits[i] > t):
            bin_limit_inf = bin_limits[i-1]
            bin_limit_sup = bin_limits[i]
            break
    for i in range(0, len(sorted_data)):
        if (bin_limit_inf <= sorted_data[i] < bin_limit_sup):
            counter += 1
    return counter / (len(sorted_data) * (bin_limit_sup - bin_limit_inf))


margin = (data[len(data)-1] - data[0]) * 0.1
xe = np.linspace(data[0] - margin, data[len(data)-1] + margin, PLOT_POINTS)
ye = np.array(list(map(fde, xe)))

margin = (bin_limits[len(bin_limits)-1] - bin_limits[0]) * 0.1
xh = np.linspace(bin_limits[0] - margin, bin_limits[len(bin_limits)-1] + margin, PLOT_POINTS)
yh = np.array(list(map(hist, xh)))

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")

# Plots
figure, axis = plt.subplots(1, 2)

axis[0].plot(xe, ye)
axis[0].set_title('Función de distribución empírica')
plt.grid(True)

axis[1].plot(xh, yh)
axis[1].set_title('Función histograma')
plt.grid(True)

plt.show()
