import numpy as np
import matplotlib.pyplot as plt 

a = np.genfromtxt("RadialVelocities.dat", skip_header = 1)
b = np.loadtxt("datos.dat")

r = a[:, 0]
v = a[:, 1]

mb = b[0]
md = b[1]
mh = b[2]

bb = 0.2497 
bd = 5.16
ad = 0.3105
ah = 64.3

def Vo(r, mb, md, mh):
	Vo =  mb**(1/2)*r/(r**2 + bb**2)**(3/4) + md**(1/2)*r/(r**2 + (bd+ad)**2)**(3/4) + mh**(1/2)/(r**2 + ah**2)**(1/4)
	return (Vo)

plt.figure()
plt.title("Velocidades Radiales")
plt.scatter(r,v)
plt.plot(r,Vo(r, mb,md,mh), color = "orange")
plt.xlabel("Radio (kpc)")
plt.ylabel("Velocidad (km/s)")
plt.savefig("velocidades.jpg")
