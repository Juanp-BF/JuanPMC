import numpy as np 

a = np.matrix('1.0 -1.0; 1.0 1.0')


#a[0] = a[0]/a[0,0]
#a[1] = a[1] - a[0]*a[1,0]

#print(len(a[:]))
print(a[0,:])
def solucion(a):
	for i in range(len(a[0])+1):
		for j in range(len(a[:])-1):
			if(i == j and a[i,j] != 1):
				a[i] = a[i]/a[i,j]
				print (a, i, j)
			elif(j != 0 and a[j,i] != 0):
				a[j] = a[j] - a[i]*a[j,i]
				print (a, i, j)
	return a			
		
print (solucion(a))

