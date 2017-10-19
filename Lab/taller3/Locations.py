import numpy as np 
from matplotlib import pyplot as plt

a = np.loadtxt('locations.txt')

lat = a[:,0]
lon = a[:,1]

b = plt.hist(a[:,0], bins=15)
c = plt.hist(a[:,1], bins=15)

print (b[1][:])
print (b[0][:])

def range_maxLat(b):
    x = 0
    y = 0
    p = 0
    for i in range(15):
        if(b[0][i] > p):
            p = b[0][i]
            x = b[1][i]
            y = b[1][i+1]
    return x, y

def range_maxLon(c):
    x = 0
    y = 0
    p = 0
    for i in range(15):
        if(c[0][i] > p):
            p = c[0][i]
            x = c[1][i]
            y = c[1][i+1]
    return x, y

print ("El rango de longitudes en el que hay mas terremotos es: ", range_maxLon(c))
print ("El rango de latitudes en el que hay más terremotos es: ", range_maxLat(b) )
plt.show(b)
plt.show(c)
