import numpy as np 
import matplotlib.pyplot as plt

#condiciones de frontera

h = 0.01
x_min = 0.0
x_max = 1.0
n_points = int((x_max - x_min)/h)
x = np.zeros(n_points)
y = np.zeros(n_points)

def y_2prima(x, y):
	return -g/l*np.sin()

x[0] = x_min
y[0] = 0.0

x[1] = x_min + h
y[1] = y[0] + h*f_derivada(x[0], y[0])

for i in range(1, n_points-1):
	x[i+1] = x[i] + h
	y[i+1] = y[i-1] + 2*h*f_derivada(x[i], y[i])

plt.plot(x, y, 'ko')
plt.plot(x, np.tan(x))
plt.xlabel('x')
plt.ylabel('y')
plt.show()

