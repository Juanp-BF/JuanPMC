import numpy as np 
import matplotlib.pyplot as plt 
import os 
from matplotlib import animation 


b = np.genfromtxt("datos.txt")
x = b[:, 0]
u_inicial = b[:, 2]
ut8 = b[:, 3]
ut4 = b[:, 4]
ut2 = b[:, 5]


##fue necesario hacer los plots en una sola figura, pues, si no lo hacia la grafica de 1/4 T se graficaba con mucho ruido  
fig1 = plt.figure()
plt.plot(x, u_inicial)
plt.plot(x, ut8)
plt.plot(x, ut4)
plt.plot(x, ut2)
plt.show()

c = np.genfromtxt("datos1.txt")
x1 = c[:, 0]
u_inicial1 = c[:, 2]
ut81 = c[:, 3]
ut41 = c[:, 4]
ut21 = c[:, 5]

fig2 = plt.figure()
plt.plot(x1, u_inicial1)
plt.plot(x1, ut81)
plt.plot(x1, ut41)
plt.plot(x1, ut21)
plt.show()


fig = plt.figure()
ax = plt.axes(xlim = (0.0, 0.65), ylim = (-2.0, 2.0))
line, = ax.plot([], [])

def init():
	line.set_data([],[])
	return line,

def simulate(j):
	os.system(" cc Ondas.c -lm -o Ondas.x")
	os.system("echo %d| ./Ondas.x" %j)
	a = np.genfromtxt("datos1.txt")
	x = a[:, 0]
	u_presente = a[:, 1]
	line.set_data(x, u_presente)
	return line, 

anim = animation.FuncAnimation(fig, simulate, init_func=init,
                               frames=500, interval=20, blit=True)

anim.save('basic_animation.mp4', fps=100, extra_args=['-vcodec', 'libx264'])



