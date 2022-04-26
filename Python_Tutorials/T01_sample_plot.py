# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:21:34 2021

@author: Admin
"""
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# Ploting figure
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='y=sin(2\pi t)',
       title='About as simple as it gets, folks')
ax.grid()
fig.savefig("test.png")
plt.show()

# Ploting test figure
plt.figure()
plt.plot(range(10), 'o')
plt.show()
