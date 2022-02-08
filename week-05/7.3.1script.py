# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:06:56 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt

from numpy.random import random as rng
from scipy.special import factorial
from numpy.random import default_rng

rng = default_rng()
rand = rng.random


l = np.arange(0,18,.1)
#print(l)

pl = np.exp(-8) * 8**l / factorial(l)

plt.plot(l , pl)

# Define the problem.
Ntrials = 1000
Nflips = 100


x=np.zeros(Ntrials)
for N in np.arange(Ntrials):
    flips = 2*(rand(Nflips) < 0.08) - 1
    x = flips.sum()
    H = 100 + x


plt.hist(H,10)
print(x)
print(H)




