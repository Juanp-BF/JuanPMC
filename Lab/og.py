import numpy as np
import matplotlib.pyplot as plt
import math 


lower_limit = 0.0
upper_limit = 10.0

# funcion a integrar
def function(x, y):
    return 4/math.pi * np.exp(- (x**2) - (y**2))


# Solucion analítica
def exact(x):
    return -np.exp(-x)
    
# Calculamos el error absoluto entre el valor real de la integral y el calculado por los diferentes métodos.
def error(real, calculated):
    return abs((real-calculated)/real)

    
# Calcular la integral usando MonteCarlo
def montecarlo(f, a, b, n):    
	x = (b-a)*np.random.random(n)
	y = (b-a)*np.random.random(n)
	f_eval = f(x, y)
	result = f_eval.mean()*((b-a)**2)
	return np.log10(n), result

# Calcular la integral usando metodo de trapezoides
def trapezoid(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = np.linspace(a, b, n+1)
    h = (b-a)/n
    result = 0
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or i == n:
                if j == 0 or j == n:
                    weight = (h**2)/4
                    result += f(x[i], y[j])*weight
                else:
                    weight = (h**2)/2
                    result += f(x[i],y[j])*weight
            elif j == 0 or j == n:
                weight = (h**2)/2
                result += f(x[i],y[j])*weight
            else:
                weight += (h**2)
                result += f(x[i],y[j])
    return np.log10(n**2), result


# Vamos a calcular la integral
def integrate(func, a, b, n):
# Llamamos todas la funciones que creamos para calcular la integral. Recordemos que estas funciones retornan dos numeros: el primero es el logaritmo del numero entero usado para integrar y segundo es el valor de la integral calculado.
    montecarlo_results = montecarlo(func, a, b, n)
    trapezoid_results = trapezoid(func, a, b, n)
#    simpson_results = simpson(func, a, b, n)
#    simpson38_results = simpson38(func, a, b, n)
    
    # creamos una lista con los resultados de las 4 funciones
    results = [montecarlo_results, trapezoid_results]
    #en la lista "numbers" guardamos los resultados de las integrales por los diferentes metodos
    numbers = [item[0] for item in results]
    #en la lista "errors" guaramos el error de nuestro cálculo con respecto al valor exacto de la integral.
    errors = [np.log10(error(exact_value, item[1])) for item in results]
    
    
    return numbers, errors


#este será el calor exacto de la integral
exact_value = exact(upper_limit) - exact(lower_limit)

#creamos una lista de 20 puntos entre 0 y 10^6
points = 20
numbers = np.logspace(0, 4, points)


#estas listas vacias las usaremos para guardar nuestros valores finales
values_buffer = [[],[],[],[]]
numbers_buffer = [[],[],[],[]]

#estos nombres los usaremos para etiquetar las graficas
names = ["MonteCarlo","Trapezoid", "Simpson", "Simpson 3/8"]

#Ahora inplementaremos la función "integrate" 20 veces recorriendo 6 órdenes de magnitud.
for n in numbers:
    numbers, results = integrate(function, lower_limit, upper_limit, int(n))
    for (values_list, numbers_list, number, result) in zip(values_buffer, numbers_buffer, numbers, results): #Explicar cómo funciona "for" "in zip".
        values_list.append(result)
        numbers_list.append(number)
        
# Graficamos
for (values_list, numbers_list, name) in zip(values_buffer, numbers_buffer, names):
    plt.plot(numbers_list, values_list, "-o", label=name)

plt.legend(loc=3)
plt.xlabel("$\log_{10}n$")
plt.ylabel("$\log_{10}\epsilon$")
plt.grid()
plt.savefig("plots.pdf")
plt.show()
