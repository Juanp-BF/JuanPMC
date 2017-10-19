import numpy as np
import matplotlib.pyplot as plt
import math 


lower_limitx = 0.0
upper_limitx = 1.0
lower_limity = 0.0
upper_limity = np.pi
# funcion a integrar
def function(x, y):
	f = (x + np.cos(y)*x)**3
	return f

def montecarlo(f, a, b, c, d, n):    
	x = (b-a)*np.random.random(n)
	y = (d-c)*np.random.random(n)
	f_eval = f(x, y)
	result = f_eval.mean()*((b-a)*(d-c))
	return result

def trapezoid(f, a, b, c, d, n):
	x = np.linspace(a, b, n+1)
	y = np.linspace(c, d, n+1)
	h1 = (b-a)/n
	h2 = (d-c)/n
	result = 0
	for i in range(n+1):
		for j in range(n+1):
			if i == 0 or i == n:
				if j == 0 or j == n:
					weight = (h1*h2)/4
					result += f(x[i], y[j])*weight
				else:
					weight = (h1*h2)/2
					result += f(x[i],y[j])*weight
			elif j == 0 or j == n:
				weight = (h1*h2)/2
				result += f(x[i],y[j])*weight
			else:
				weight = (h1*h2)
				result += f(x[i],y[j])*weight
	return result


montecarlo = montecarlo(function, lower_limitx, upper_limitx, lower_limity, upper_limity, 10000000)

trapezoides = trapezoid(function, lower_limitx, upper_limitx, lower_limity, upper_limity, 1000)

print ('el valor de la integral con el metodo de montecarlo es ', montecarlo, ' y esta la calculada a partir de trapezoides ', trapezoides)

