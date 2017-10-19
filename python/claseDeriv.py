import numpy as np 

x = int(input("De el púnto en el que quiere evaluar "))
h = float(input("De el tamaño del intervalo "))


def f(x):
	return np.exp(-(x**2))

def derivada(f, h, x):
	ff = (f(x+h) - f(x))/h
	return ff	

def derivadaC(f, h, x):
	fc = (f(x+h) - f(x-h))/2*h
	return fc	
def ceros(f, x, n)
	
print(derivada(f, h, x))
print(derivadaC(f, h, x))
