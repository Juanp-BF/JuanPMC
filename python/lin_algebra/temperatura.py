import numpy as np 

a = np.loadtxt('room-temperature.csv', delimiter=',', skiprows=1, usecols=range(1,5))

T1 = a[: , 0]
T2 = a[: , 1]
T3 = a[: , 2]
T4 = a[: , 3]

ta = np.transpose(a)

ca = np.cov(ta)

n = 4

def cov(a, n):
	cov = np.ones((n,n))
	for i in range(len(a[:])):
		for j in range(len(a[0])):
			cov[j,i] = np.sum((a[i] - np.average(a[i]))*(a[j] - np.average(a[j])))
			cov1=cov/(len(a[:])-1)
	return cov

print(cov(a, n))
