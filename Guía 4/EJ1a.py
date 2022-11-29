# Función de probabilidad para la variable Y = 2X - 2, con:
# px(x) = 2x/9 {0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1}

import time
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
    y.append(2*x[i]-1)
    px.append(x[i]*2/9)
    print ("{:0.3f}   {:0.3f}   {:0.3f}".format(x[i], y[i], px[i]))

print()

print("{:<7} {:<7}".format("y", "py(y)"))
for i in range(0, 9):
    py.append((y[i]+1)/9)
    print ("{:0.3f}   {:0.3f}".format(y[i], py[i]))

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
