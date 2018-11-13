'''
Created on Nov 12, 2018

@author: dabrown
'''

from math import cos, sin, pi, sqrt
from numpy import sinc
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    pass

    ####### get HPBW for H plane ###########
    angle = 0
    dAngle = 0.01
    
    maxValue = 0
    maxAngle = 0
    for indx in range(0,360):
        angle = indx * 2 * pi / 360
        value = -cos(pi*sin(angle))/((pi*sin(angle))**2 - (pi/2)**2)
        if value > maxValue:
            maxValue = value
            maxAngle = angle
    
    angle = 0
    while(True):
        value = -cos(pi*sin(angle))/((pi*sin(angle))**2 - (pi/2)**2)
        if value < maxValue / sqrt(2):
            break
    
        angle += dAngle
    
    print(2*angle * 180 / pi)
    print(value)
    print(maxValue, maxAngle)
    
    
    
    ############ plotting the planes ##########
    # FOR E PLANE
    # phi = pi/2
    l1 = 3
    l2 = 2
    
    phi = pi / 2
    
    eField = []
    eAngle = []
    for indx in range(0,180):
        theta = indx * pi / 180
        alpha = pi * l2 * cos(theta)
        chi = pi * l1 * sin(theta) * cos(phi)
        beta = (sin(alpha) / alpha) * ( cos(chi) / (chi ** 2 - (pi/2)**2) )
        value = l1 * l2 * sin(phi) * beta
        
        eField.append(abs(value))
        eAngle.append(theta)
        
    eField = eField/np.max(eField)
    plt.figure()
    plt.plot(eAngle, eField)
    plt.xlabel(r'$\theta$')
    plt.ylabel('Amplitude')
    plt.title('E-Plane')
    
    # FOR H PLANE
    # phi = 0    
    phi = 0
    
    eField = []
    eAngle = []
    for indx in range(0,180):
        theta = indx * pi / 180
        alpha = pi * l2 * cos(theta)
        chi = pi * l1 * sin(theta) * cos(phi)
        beta =  sin(alpha)/alpha * ( cos(chi) / (chi ** 2 - (pi/2)**2 ) )
        value = l1 * l2 * sin(theta)*cos(phi) * beta
        
        eField.append(abs(value))
        eAngle.append(theta)
    
    eField = eField/np.max(eField)
    plt.figure()
    plt.plot(eAngle, eField)
    plt.title("H-Plane")
    plt.xlabel(r'$\theta$')
    plt.ylabel('Amplitude')
    
    
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    