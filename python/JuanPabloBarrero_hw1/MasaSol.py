import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig =plt.figure()
ax = fig.add_subplot(111, projection = '3d')

h = 1.0

MO = np.loadtxt('MarsOrbit.dat')
EO = np.loadtxt('EarthOrbit.dat')

au = 149597870700 

tm = MO[:,0]*31557600
xm = MO[:,1]*au
ym = MO[:,2]*au
zm = MO[:,3]*au

rm = np.sqrt(xm**2 + ym**2 + zm**2)

te = EO[:,0]*31557600
xe = EO[:,1]*au
ye = EO[:,2]*au
ze = EO[:,3]*au

re = np.sqrt(xe**2 + ye**2 + ze**2)

ax.plot(xm, ym, zm, label = 'Orbita Marte', color = 'blue')
ax.plot(xe, ye, ze, label = 'Orbita Tierra', color = 'black')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('Orbitas.pdf')
plt.show()

xve = np.zeros(len(xe)-2)
yve = np.zeros(len(ye)-2)
zve = np.zeros(len(ze)-2)
for i in range(1, len(xe)-1):	
	xve[i-1] = (xe[i+1]-xe[i-1])/(te[i+1]-te[i-1])
	yve[i-1] = (ye[i+1]-ye[i-1])/(te[i+1]-te[i-1])
	zve[i-1] = (ze[i+1]-ze[i-1])/(te[i+1]-te[i-1])



xvm = np.zeros(len(xm)-2)
yvm = np.zeros(len(ym)-2)
zvm = np.zeros(len(zm)-2)
for i in range(1, len(xm)-1):		
	xvm[i-1] = (xm[i+1]-xm[i-1])/(tm[i+1]-tm[i-1])
	yvm[i-1] = (ym[i+1]-ym[i-1])/(tm[i+1]-tm[i-1])
	zvm[i-1] = (zm[i+1]-zm[i-1])/(tm[i+1]-te[i-1])

xam = np.zeros(len(xvm)-2)
yam = np.zeros(len(yvm)-2)
zam = np.zeros(len(zvm)-2)
for i in range(1, len(xvm)-1):
	xam[i-1] = (xvm[i+1] - xvm[i-1])/(tm[i+1]-tm[i-1])
	yam[i-1] = (yvm[i+1] - yvm[i-1])/(tm[i+1]-tm[i-1])
	zam[i-1] = (xvm[i+1] - xvm[i-1])/(tm[i+1]-tm[i-1])

xae = np.zeros(len(xve)-2)
yae = np.zeros(len(yve)-2)
zae = np.zeros(len(zve)-2)
for i in range(1, len(xve)-1):
	xae[i-1] = (xve[i+1] - xve[i-1])/(te[i+1]-te[i-1])
	yae[i-1] = (yve[i+1] - yve[i-1])/(te[i+1]-te[i-1])
	zae[i-1] = (zve[i+1] - zve[i-1])/(te[i+1]-te[i-1])
	

am = np.sqrt(xam**2 + yam**2 + zam**2)
ae = np.sqrt(xae**2 + yae**2 + zae**2)	

def masaSolT(ae, re):
	G = 6.674*10**(-11)
	m = ae*(re[2	:-2]**2)/G
	ms = np.mean(m)
	return ms

def masaSolM(am, rm):
	G = 6.674*10**(-11)
	m = am*(rm[2	:-2]**2)/G
	ms = np.mean(m)
	return ms

print (masaSolT(ae, re), 'es la masa del sol en Kg medida a partir de la órbita de la Tierra')

print (masaSolM(am, rm), 'es la masa del sol en Kg medida a partir de la órbita de Marte')












