'''
Created on Nov 14, 2018

@author: dabrown
'''

import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi

if __name__ == '__main__':
    pass
    
    lam = 12
    w = 4.7434
    k = 2 * pi / lam
    
    thetas = np.linspace(0,pi,500)
    dTheta = thetas[1]-thetas[0]
    
    sum = 0
    for theta in thetas:
        first = sin(k*w*cos(theta)/2) /  cos(theta)
        first = first * first
        value = first * sin(theta)**3
        sum = sum + value * dTheta
        
    print(sum)
    