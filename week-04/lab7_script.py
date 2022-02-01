# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 10:55:57 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt

from numpy.random import random as rng

num_steps=1000

plt.figure()

x_step1=rng(num_steps) > 0.5
y_step1=rng(num_steps) > 0.5
x_step1 = 2*x_step1 - 1 
y_step1 = 2*y_step1 - 1 


x_position1 = np.cumsum(x_step1)
y_position1 = np.cumsum(y_step1)



plt.subplot(2,2,1)
plt.plot(x_position1,y_position1, 'k')
plt.axis('equal')
plt.xlim(-10,10)
plt.ylim(-10,10)

x_step2=rng(num_steps) > 0.5
y_step2=rng(num_steps) > 0.5
x_step2 = 2*x_step2 - 1 
y_step2 = 2*y_step2 - 1 


x_position2 = np.cumsum(x_step2)
y_position2 = np.cumsum(y_step2)



plt.subplot(2,2,2)
plt.plot(x_position2,y_position2,'r')
plt.axis('equal')
plt.xlim(-10,10)
plt.ylim(-10,10)

x_step3=rng(num_steps) > 0.5
y_step3=rng(num_steps) > 0.5
x_step3 = 2*x_step3 - 1 
y_step3 = 2*y_step3 - 1 


x_position3 = np.cumsum(x_step3)
y_position3 = np.cumsum(y_step3)



plt.subplot(2,2,3)
plt.plot(x_position3,y_position3,'g')
plt.axis('equal')
plt.xlim(-10,10)
plt.ylim(-10,10)

x_step4=rng(num_steps) > 0.5
y_step4=rng(num_steps) > 0.5
x_step4 = 2*x_step4 - 1 
y_step4 = 2*y_step4 - 1 


x_position4 = np.cumsum(x_step4)
y_position4 = np.cumsum(y_step4)



plt.subplot(2,2,4)
plt.plot(x_position4,y_position4,'y')
plt.axis('equal')
plt.xlim(-10,10)
plt.ylim(-10,10)


plt.savefig("Lab 7.1 subplot random walks.pdf")