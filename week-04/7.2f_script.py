# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:27:04 2022

@author: benja
"""


import numpy as np
import matplotlib.pyplot as plt

from numpy.random import random as rng

num_steps=4000
num_walks=1000


x_final=np.zeros(num_walks)
y_final=np.zeros(num_walks)
displacement=np.zeros(num_walks)




Nwalks=1

for i in range(1000):
    Nwalks = i  
    #print(Nwalks)
    
    

    x_step=rng(num_steps) > 0.5
    y_step=rng(num_steps) > 0.5
    x_step = 2*x_step - 1 
    y_step = 2*y_step - 1 

    x_position = np.cumsum(x_step)
    y_position = np.cumsum(y_step)

    x_final[i] = x_position[-1]
    y_final[i] = y_position[-1]
    displacement[i] = np.sqrt(x_position[-1]**2 + y_position[-1]**2)
    
    
disp = np.mean(displacement**2)

print("The mean value of displacement**2 for 4000 steps = ", disp)


