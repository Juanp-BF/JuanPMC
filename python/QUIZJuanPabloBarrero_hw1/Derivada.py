import numpy as np 
import matplotlib.pyplot as plt

a = np.loadtxt('Balon.dat')

t = a[:, 0]

x = a[:, 1]


vel = np.zeros(len(x)-2)
for i in range (1, len(x)-1):
	vel[i-1] = (x[i+1] - x[i-1])/(t[i+1]-t[i-1])

v = (0.19 - 0)/(0.02)

plt.plot(t[0:-2], vel)
plt.xlabel('Tiempo en segundos')
plt.ylabel('velocidad en metros/segundo')
plt.title('Tiempo vs Velocidad')
plt.savefig('Derivada.pdf')

print (vel, v)
