import numpy as np 
from scipy import fftpack
from scipy.signal import convolve2d
import matplotlib.pyplot as plt  

im1 = plt.imread('20_popc_cho009-1.tif')
im2 = plt.imread('colesterol-1.tif')
im1 = plt.imread('ves_full_150_002-1.tif')
print(np.shape(im1))

fig = plt.figure(1, figsize=(9.5, 9))
plt.imshow(im1)
plt.imshow(im2)
plt.show()
