import numpy as np
import matplotlib.pyplot as plt 

t = np.zeros(4)
v = [0, 45.948,119.985,231.497]
t1 = 7.0
a = np.matrix('4.0 2.0 1.0 45.948 ; 25.0 5.0 1.0 119.985 ; 81.0 9.0 1.0 231.497')
t2 = [0, 2.0, 5.0, 9.0]

for i in range(4):
	t[i] = t2[i]
print (t)
def sol(a):
	#Diagonalización triángulo inferiror
	for i in range(len(a[0])+1):
		for j in range(0, len(a[:])):
			if(i == j and j == 0):
				a[i] = a[i]/a[i,j]
			elif(j >= i and j+i != len(a[:]) and a[i+j,i] != 0):
				a[i+j] = a[i+j] - a[i]*a[i+j,i]
				a[i+j] = a[i+j]/a[i+j,i+j]
	#Diagonalización triángulo superior	
	for i in range(len(a[0])+1):
		for j in range(0, len(a[:])):
			if(j > i and i+j != len(a[:])):			
				a[i] = a[i] - a[i+j]*a[i,i+j]
			elif(i == j and j != 0 and j+i != len(a[:])):
				a[i] = a[i] - a[i+j]*a[i,i+j]
				
	return a

def vel(t, sol):
	a1 = sol[0,3]
	a2 = sol[1,3]
	a3 = sol[2,3]
	vel = a1*t**2 + a2*t + a3
	return vel

plt.plot(t, vel(t, sol(a)))
plt.scatter(t, v, c='red')
plt.title("Velocidades del cohete contra tiempo")
plt.ylabel("V(m/s)")
plt.xlabel("T(s)")
plt.savefig("VelocidadCohete.pdf")
	
print ("Los valores de a1, a2 y a3, respectivamente, son ", sol(a)[0,3],",",sol(a)[1,3],",",sol(a)[2,3]," y el valor de la velocidad en el segundo 7 es", vel(t1, sol(a)))

