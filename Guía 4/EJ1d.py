# Función de probabilidad para la variable Y = 64X^2 - 96X + 128, con:
# px(x) = 2x/9 {0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1}

import time
import numpy as np
import matplotlib.pyplot as plt

# =============================================
#             PARÁMETROS INICIALES            
# =============================================

x = []
px =[]

y = []
py = []

# =============================================
#                 RESOLUCIÓN           
# =============================================
startTime = time.perf_counter_ns()

print("{:<7} {:<7} {:<7}".format("x", "y", "px(x)"))
for i in range(0, 9):
    x.append(i/8)
    y.append(64*(x[i]**2) - 96*x[i] + 128)
    px.append(x[i]*2/9)
    print ("{:0.3f}   {:0.3f}   {:0.3f}".format(x[i], y[i], px[i]))

print()

print("{:<7} {:<7}".format("y", "py(y)"))
_y = []
for i in range(0, 4):
    _y.append(y[i])
    _py = 0
    _py = ((96 - np.sqrt(9216 - 256 * (128 - y[i])))/128) * 2/9
    py.append(_py)
    print("{:0.3f}   {:0.3f}".format(y[i], py[i]))
for i in range(4, 6):
    _y.append(y[i])
    _py = 0
    _py = ((96 - np.sqrt(9216 - 256 * (128 - y[i])))/128) * 2/9
    _py += ((96 + np.sqrt(9216 - 256 * (128 - y[i])))/128) * 2/9
    py.append(_py)
    print("{:0.3f}   {:0.3f}".format(y[i], py[i]))
for i in range(6, 7):
    _y.append(y[i])
    _py = 0
    _py = ((96 - np.sqrt(9216 - 256 * (128 - y[i])))/128) * 2/9
    py.append(_py)
    print("{:0.3f}   {:0.3f}".format(y[i], py[i]))
y = _y

endTime = time.perf_counter_ns()
# =============================================
#                 RESULTADOS           
# =============================================

# Prints
print("Tiempo de ejecución:", (endTime - startTime) / 1000000, "ms")

plt.figure()

plt.subplot(121)
plt.plot(x, px, 'ro')
plt.title('px')
plt.grid(True)

plt.subplot(122)
plt.plot(y, py, 'ro')
plt.title('py')
plt.grid(True)
plt.show()
