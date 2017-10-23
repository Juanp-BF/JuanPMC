import numpy as np 
import matplotlib.pylab as plt
from scipy.fftpack import fft,fftfreq

a = np.genfromtxt('funcion.dat')
t = a[:,0]
y = a[:,1]
dt = t[1]
n = 256
N = len(y)

freq = fftfreq(len(t), dt)
Transform = fft(y)

def fourier(y, N):
	resultado = np.zeros(N)
	for i in range(N-1):
		four = 0.0
		for j 	in range(N):
			four += y[j]*np.exp(-1j*np.pi*2*i*j/N)
		resultado[i] = four 
	return resultado

print(fourier(y, N))
print (t)

plt.plot(freq, fourier(y, N))
plt.show()
plt.plot(freq, Transform)
plt.show()
