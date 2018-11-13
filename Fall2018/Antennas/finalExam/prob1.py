'''
Created on Nov 13, 2018

@author: dabrown
'''

from math import pi, cos
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass

    d = 0.7784
    beta = pi/2
    
    af = []
    af2 = []
    x = []
    for degree in range(1,720*2):
        theta = degree * pi / 720 + pi/2
        u = pi * d * cos(theta)
        af.append(0.1333 * cos(u) + 0.25 * cos(3*u) + cos(5*u))
        af2.append(1.5 * cos(u) + 1.3 * cos(3*u) + 1*cos(5*u))
        x.append(theta)
    
    af = af/np.max(af)
    plt.figure()    
    plt.polar(x, af)
    
    af2 = af2/np.max(af2)
    plt.figure()
    plt.polar(x,af2)
        
    plt.show()