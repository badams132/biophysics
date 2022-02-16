# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:57:43 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sim


#impulse = np.zeros( (51, 51) )
#impulse[25, 25] = 1.0
#my_filter = np.ones( (3, 3) ) / 9
#response = sim.convolve(impulse, my_filter)

#plt.imshow('bwCat.tif')
my_filter = np.ones( (3, 3) ) / 9
my_filter1 = np.ones( (15, 15) ) / 225




#print(my_filter)


cat = plt.imread('bwCat.tif')

#plt.imshow(cat)
response = sim.convolve(cat, my_filter,mode='constant')
#plt.subplot(1,2,1)
plt.imshow(response, cmap = 'gist_gray')
plt.title("3x3 sim.convolve (greyscale)")



plt.figure()
alt_response = sim.uniform_filter(cat)
plt.imshow(alt_response, cmap = 'gist_gray')
plt.title("sim.uniform_filter (greyscale)")

plt.figure()
response1 = sim.convolve(cat, my_filter1,mode='constant')
#plt.subplot(1,2,2)
plt.imshow(response1, cmap='gist_gray')
plt.title("15x15 sim.convolve (greyscale)")
