# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:45:04 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
time = np.linspace(0,7,101)
#print(time)

B=60
A=105000
alpha=.39
beta=3

viral_load= A * np.exp(-alpha * time)+ B * (-beta*time)
#print(viral_load)

plt.plot(time, viral_load,'r')

HIVdata=np.loadtxt('HIVseries/HIVseries.csv' , delimiter=',')
#print(HIVdata)

time1=HIVdata[0:17:1,0]  # slice
print(time1)

concentration=HIVdata[0:17:1,1]
#print(concentration)

plt.plot(time1,concentration,'ko')
#plt.legend()


plt.title("HIV Infection Time Course", size='24',weight='bold')
plt.xlabel("Time in Days",weight='bold')
plt.ylabel("Concentration of Virus", weight='bold')

