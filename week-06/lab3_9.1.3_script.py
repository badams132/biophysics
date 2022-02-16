# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:23:39 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sim
from mpl_toolkits.mplot3d import Axes3D

ax = Axes3D (plt.figure())



gauss=np.loadtxt('gauss_filter.csv' , delimiter=',')


cat = plt.imread('bwCat.tif')

#plt.imshow(cat)
response = sim.convolve(cat, gauss,mode='constant')
#plt.subplot(1,2,1)
plt.figure()
plt.imshow(response)
plt.title("gauss sim.convolve")

plt.figure()
plt.imshow(response, cmap='gist_gray')
plt.title("gauss sim.convolve(greyscale)")


impulse = np.zeros( (51, 51) )
impulse[25, 25] = 1.0
my_filter = np.ones( (3, 3) ) / 9
response_dot = sim.convolve(impulse, gauss)

plt.figure()
plt.imshow(response_dot, cmap = 'gist_gray')
plt.title("gauss sim.convolve dot")


my_filter = np.ones( (3, 3) ) / 9
response_dot1 = sim.convolve(impulse, my_filter)
plt.figure()
plt.imshow(response_dot1, cmap = 'gist_gray')
plt.title("3x3 sim.convolve dot")

#plt.figure()
#ax.plot_surface(response_dot1,response_dot,my_filter)