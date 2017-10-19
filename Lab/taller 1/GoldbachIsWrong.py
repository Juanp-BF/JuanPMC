## Goldbach is wrong

import PrimesLessThan as nplt
import IsPrime as isp
import math

y = 0
m = 9	
n = 0
while (y == 0):	
	if(isp.IsPrime(m) == 1):
		m += 2
	else:
		for i in range(len(nplt.PrimesLessThan(m))):
			if(math.sqrt((m - nplt.PrimesLessThan(m)[i])/(2)) is int):
				m+=2
				break
			else:
				if(i == len(nplt.PrimesLessThan(m))):
					y = 1

print(m)
			
				

