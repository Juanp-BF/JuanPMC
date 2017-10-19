import numpy as np
import random

min_x = float(input("ingrese el límite inferior: "))
max_x = float(input("ingrese el Límite superior: "))

def func(x):
	f = ((5*x**3 - 3*x) / 2)**2
	return f

n=1000000
def integral(func, n):
	
	x = np.random.random(n) * (max_x - min_x) + min_x
	y = func(x)
	
	integral = np.average(y) * (max_x - min_x)
	return integral

i = 2/7

def errorP(integral, i):
	err = np.abs((integral(func, n) - i)/ i) * 100
	return err 


print ("la integral es: ", integral(func, n))
print ("el valor real de integral entre -1 y 1 es: ", i)

if min_x == -1 and max_x == 1:
	print ("el error porcentual es: ", errorP(integral, i))
