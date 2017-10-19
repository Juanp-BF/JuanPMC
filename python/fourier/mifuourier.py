import numpy as np 
import matplotlib.pylab as plt
from scipy.fftpack import fft,fftfreq

n = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
y = np.cos(2* np.pi *f*t)
N = len(y)

freq = fftfreq(n, dt)
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

plt.plot(freq, fourier(y, N))
plt.show()
plt.plot(freq, Transform)
plt.show()
