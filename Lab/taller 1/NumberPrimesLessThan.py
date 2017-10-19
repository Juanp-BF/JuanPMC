##Tercer script en el taller
import matplotlib.pyplot as plt
import numpy as np
import scipy as scipy
import PrimesLessThan as plss
from scipy import special



x = list(range(1, 1000))
def NumberPrimesLessThan(x):
	pix = []
	for i in range(0, len(x)):
		pix.append(len(plss.PrimesLessThan(x[i])))
	return pix
print (NumberPrimesLessThan(x))
plt.plot(x, NumberPrimesLessThan(x))
plt.plot(x, scipy.special.expi(np.log(x)))
plt.show()
plt.title("bueno")
