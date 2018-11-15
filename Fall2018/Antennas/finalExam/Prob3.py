'''
Created on Nov 15, 2018

@author: dabrown
'''

import matplotlib.pyplot as plt 
from math import cos, sin, pi
import numpy as np

if __name__ == '__main__':
    pass

    ka = 2*pi * 3
    kb = 2*pi * 2

    # first plot my stuff for E and H planes
    # mine H plane is E_theta for theta = pi/2
    
    phis = np.linspace(0,2*pi,500)
    theta = pi/2
    
    values = []
    for phi in phis:
        X = ka / 2 * sin(theta) * sin(phi)
        value = abs(cos(phi)* cos(X) / (X**2 - (pi/2)**2))
        values.append( value )
        
    values = values/np.max(values)
    plt.figure()
    plt.plot(phis, values)
    plt.title(r'WaveGuide in $\hat{a}_x$ for H-Plane')
    plt.ylabel('Normalized |E|')
    plt.xlabel(r'$\phi$')
    plt.savefig('prob3_mine_Hplane.png')
    
    
    # mine E plane is E_phi for phi = 0
    
    thetas = np.linspace(0,2*pi,500)
    phi = 0
    
    values = []
    for theta in thetas:
        X = 0
        Y = kb/2 * cos(theta)
        value = abs( cos(phi)* cos(X) / (X**2 - (pi/2)**2) * sin(Y)/Y)
        values.append( value )
        
    values = values/np.max(values)
    plt.figure()
    plt.plot(thetas, values)
    plt.title(r'WaveGuide in $\hat{a}_x$ for E-Plane')
    plt.ylabel('Normalized |E|')
    plt.xlabel(r'$\theta$')
    plt.savefig('prob3_mine_Eplane.png')
    
    
    ########## from book for E and H planes ###########
    # H plane (x-z) so phi = 0
    phi = 0
    
    thetas = np.linspace(0,2*pi,500)
    
    values = []
    for theta in thetas:
        X = ka / 2 * sin(theta) * cos(phi)
        Y = 0
        value = abs(cos(theta) * cos(phi) * cos(X) / (X**2 - (pi/2)**2))
        values.append( value )
        
    values = values/np.max(values)
    plt.figure()
    plt.plot(phis, values)
    plt.title(r'WaveGuide (book) in $\hat{a}_z$ for H-Plane')
    plt.ylabel('Normalized |E|')
    plt.xlabel(r'$\phi$')
    plt.savefig('prob3_Hplane.png')
    
     
    # E_phi for y-z , so phi = pi/2
     
    thetas = np.linspace(0,2*pi,500)
    phi = pi/2
     
    values = []
    for theta in thetas:
        X = 0
        Y = kb/2 * sin(theta) * sin(phi)
        if(Y == 0):
            sincY = 1
        else:
            sincY = sin(Y)/Y
        value = abs(sin(phi)* cos(X) / (X**2 - (pi/2)**2) * sincY)
        values.append( value )
         
    values = values/np.max(values)
    plt.figure()
    plt.plot(thetas, values)
    plt.title(r'WaveGuide (book) in $\hat{a}_z$ for E-Plane')
    plt.ylabel('Normalized |E|')
    plt.xlabel(r'$\theta$')
    plt.savefig('prob3_Eplane.png')
     
    
    
    plt.show()
        
        