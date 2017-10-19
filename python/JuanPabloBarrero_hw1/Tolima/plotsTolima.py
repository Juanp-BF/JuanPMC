import numpy as np 
import matplotlib.pyplot as plt
	
a = np.loadtxt('DatosMarzo.txt')
b = np.loadtxt('GRF_VS_EQ.txt')

GRFm = a[:, 0]
LEQm = a[:, 1]

GRFt = b[:, 0]
LEQt = b[:, 1]

plt.scatter(LEQm, GRFm , s=100, color = "green")
plt.scatter(LEQt, GRFt , s=10, color = "black")
plt.xlabel('Largest Earthquake')
plt.ylabel('Glacier and Rock Fall')
plt.title('GRF vs LEQ')
plt.show()

