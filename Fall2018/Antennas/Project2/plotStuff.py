'''
Created on Nov 11, 2018

@author: DougBrownWin
'''

from math import pi, sin, cos, ceil
from cmath import exp
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    pass

    # put coeficents here
    am = [1,2,3]
    
    # spacing here
    d = 1/2
    
    
    
    dTheta = 2 * pi / 720

    # get array factor from equation a coefficients
    af = []
   
    for indxTheta in range(0,720):
        sum = 0
        theta = dTheta * indxTheta 
        for n in range(-len(am)+1, len(am)):
            if(n<0):
                an = am[-n]
            else:
                an = am[n]
            sum += an * exp(1j*n*(2*pi*d*cos(theta) - pi/2))
        
        af.append(abs(sum))
    
    
    
    af = af / np.max(af)
    x = np.linspace(0, 2 * pi, num=720)
    
    
    plt.figure()
    plt.polar(x, af)
    plt.title('Array Factor')
    plt.xlabel(r'$\theta$')

    plt.show()    
    
    
    