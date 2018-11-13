'''
Created on Nov 4, 2018

@author: dabrown
'''

from math import pi, sin, cos, ceil
from cmath import exp
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':
    pass
    
    angles = 720
    bw = 360 / (2 * pi) * pi / 10
    
    am = np.array([0.85514, -0.74058, 1, -0.53572, 0.57243])
    am = am / np.max(am)
    print(am)
    N = len(am)*2 - 1
    d = 2 / (N-1)
    
    dTheta = 2 * pi / 720
    
    
    # get array factor from equation a coefficients
    af = np.zeros((720,1))
   
    for indxTheta in range(0,720):
        sum = 0
        theta = dTheta * indxTheta 
        for n in range(-len(am)+1, len(am)):
            if(n<0):
                an = am[-n]
            else:
                an = am[n]
            sum += an * exp(1j*n*(2*pi*d*cos(theta) - pi/2))
        
        af[indxTheta] = (abs(sum))
    
    ratio = af[0] / af[360]
    
    # get hpbw
    max = af[0]
    for indxTheta in range(0,45*2):
        value = af[indxTheta]
        if value > max / 2:
            hpbwAngle = indxTheta * dTheta
        
    hpbwAngle *= 2
            
    # get hpbw2 of back side
    max2 = af[360]
    for indxTheta in range(360,460):
        value = af[indxTheta]
        if value > max2 / 2:
            hpbw2Angle = indxTheta * dTheta
        else:
            break
    hpbw2Angle =  hpbw2Angle - pi
    hpbw2Angle *= 2
        
    print('Ratio is %f' % (ratio))
    print('Actual hpbw is %f' % (hpbwAngle))
    print('Actual hpbw2 is %f' % (hpbw2Angle))
    
    af = af / np.max(af)
    
    x = np.linspace(0, 2 * pi, num=720)
    plt.figure()
    plt.polar(x, af)
    plt.title('Array Factor')
#     plt.savefig('af.png')
            

    
    plt.show()    
        
        
        