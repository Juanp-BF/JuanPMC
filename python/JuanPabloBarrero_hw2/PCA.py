import numpy as np 
import matplotlib.pyplot as plt

a = np.loadtxt('siliconwaferthickness.csv', skiprows = 1, delimiter = ",")
norm = np.zeros(np.shape(a))
x = np.linspace(0, 1000	, len(a))

print(len(a)) 
for i in range(len(a[0,:])):
	norm[:,i] = (a[:,i] - np.mean(a[:,i]))/(np.std(a[:,i]))

plt.figure()
plt.plot(norm[:, 0])
plt.plot(norm[:, 1])
plt.plot(norm[:, 2])
plt.plot(norm[:, 3])
plt.plot(norm[:, 4])
plt.plot(norm[:, 5])
plt.plot(norm[:, 6])
plt.plot(norm[:, 7])
plt.plot(norm[:, 8])
plt.title("Datos del grosor de un waffer de silicona")
plt.ylabel('Grosor')
plt.savefig('ExploracionDatos.pdf')


cov = np.zeros([9,9])
for i in range(len(norm[0,:])):	
	for j in range(len(norm[0,:])):
		cov[i,j] = sum((norm[:, j] - np.mean(norm[:,j]))*(norm[:, i] - np.mean(norm[:,i])))/(len(norm[:,0])-1)

EVal1, EVec1 = np.linalg.eig(cov)

EVal2 = np.sort(EVal1)
EVal = EVal2[::-1]

EVec = np.zeros([9,9])
cont = 4	
for i in range(0,9):	
	if(i >= 4):	
		EVec[:,i] = EVec1[:,i+cont]
		cont -= 2
	else:
		EVec[:,i] = EVec1[:,i]


print ("Los valores propios de la matriz de covarianza es: ", EVal , " y los vectores propios son ", EVec, " para describir la variabilidad de los datos son necesarias 4 componentes.")

nsis = np.dot(norm, EVec[:,:-7])

plt.figure()
plt.scatter(nsis[:,0],nsis[:,1])
plt.title('datos generales en el sistema de eigenvectores')
plt.ylabel('Componente principal 1')
plt.xlabel('Componente principal 2')
plt.savefig('PCAdatos.pdf')



c = ['b','c','r','k','g','orange','y','m','purple']

plt.figure()
for i in range(9):
	plt.scatter(EVec[i,0],EVec[i,1],color=c[i], label='G%d' % i)
	plt.legend(loc='best')
plt.xlabel('e1')
plt.ylabel('e2')
plt.savefig('PCAvaraibles.pdf')

print('Las variables que estan correlacionadas son G0, G1, G2, G3 y G4 ')

