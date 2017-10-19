## Sript 2 del taller de Laboratorio
import IsPrime as pri
n = int(input("n = "))

def PrimesLessThan(n):
	primos = []
	j = 1
	while(j < n):
		if(pri.IsPrime(j) == 1):
			primos.append(j)
			j = j+1
		else:
			j = j+1
	return primos
print (PrimesLessThan(n))

