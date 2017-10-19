import numpy as np
import matplotlib.pyplot as plt

m = np.loadtxt('magnitudes.txt')

a = [ pow(10,i) for i in range(5) ]
b = plt.hist(m, bins=5)

print (b[0])
plt.show(b)
x = np.cumsum(b[0])
print(x)

plt.plot(a, x)
plt.show()
