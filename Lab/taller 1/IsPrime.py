# Primer script.
n = int(input("n = "))
def IsPrime(n):
	if (n == 2 or n == 3):
		return 1
	for i in range (2, n-1, 1):
		if(n%i == 0):
			return 0					
	return 1

print (IsPrime(n))
