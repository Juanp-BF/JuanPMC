import numpy as np 
import matplotlib.pyplot as plt
import scipy.linalg as linalg
a = np.genfromtxt('datacredit.csv')

def esta(a):
	datacredit = np.zeros(np.shape(a))
	for i in range(np.shape(a)[1]):
		prom = np.mean(a[:,i])
		desv = np.std(a[:,i])
		datacredit[:,i] = (a[:,i]-prom)/(desv) 
	return datacredit

MC = np.cov(esta(a).T)

EigVa, 	EigVe = linalg.eig(MC)

val = np.sort(EigVa)[::-1]

plt.plot(val)
plt.show()

print(np.abs(MC))
print(EigVe)
print 
