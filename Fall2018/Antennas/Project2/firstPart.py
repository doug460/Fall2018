'''
Created on Nov 4, 2018

@author: dabrown
'''

from math import pi, sin, cos, ceil
from cmath import exp
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    pass
    
    angles = 720
    bw = 360 / (2 * pi) * pi / 10
    
    
    
    sf = np.ones((720))
    # side lobe
    for indx in range(2*round(bw/2),4*round(bw/2)):
        sf[indx] = 0
        sf[angles - indx] = 0
         
    for indx in range(4*round(bw/2), 361):
        sf[indx] = 0
        sf[angles - indx] = 0       
    for indx in range(360, 360+2*round(bw/2)):
        sf[indx] = 0.25;
        sf[angles-indx] = 0.25
        
    for indx in range(360 + 2 * round(bw/2), 360 + 4 * round(bw/2)):
        sf[indx] = 0;
        sf[angles - indx] = 0;
        
        
    
    
    x = np.linspace(0, 2 * pi, num=720)

    plt.plot(x, sf)
    plt.title('Desired Pattern')
    
    kz = 0 # symetric pattern
    I = []
        
    # calculate first integral for current distribution
    # here the length is really only 3 lambda
    N = 51
    dTheta = 2 * pi / 720
    d = 1/2
    l = d * N
    dz = l / 720
    for indxZ in range (0,720):
        value = 0+0j
        z = dz * indxZ
        for indxTheta in range(0,720):
            theta = indxTheta * dTheta
            value += sf[ indxTheta ] * exp( -1j * z * theta) * dTheta
        
        I.append(value / (2 * pi))
    
    sfFinal = []
    max = 0
    side = 0
    mid = 0
    midAngle = 0
    maxAngle = 0
    for indxTheta in range(0,720):
        value = 0
        theta = indxTheta * dTheta
        for indxZ in range(0,720):
            z = indxZ * dz
            value += I[indxZ] * exp( 1j * theta * z )
        
        value = abs(value)
            
        # get max
        if value > max:
            max = value
            
        # get sidelobe
        if indxTheta > 50 and indxTheta < 200:
            if value > side:
                side = value
                
        # get mid value
        if indxTheta > 300 and indxTheta < 500:
            if value > mid:
                mid = value
                midAngle = theta
            
        sfFinal.append(value)
        
    # get hpbw
    for indxTheta in range(0,200):
        value = sfFinal[indxTheta]
        if value > max / 2:
            hpbwAngle = indxTheta * dTheta
            
    hpbw = 2 * hpbwAngle
        
    # get mid hpbw
    for indxTheta in range(300,500):
        value = sfFinal[indxTheta]
        if value > mid / 2:
            hpbwAngle = indxTheta * dTheta
    
    hpbw2 = abs(pi - hpbwAngle) * 2
    
    # get excitation coefficients
    am = []
    for indxM in range(ceil(N/2)):
        value = 0
        for indxTheta in range(0,720):
            theta = dTheta * indxTheta
            value += sfFinal[indxTheta] * exp(-1j * indxM * theta) * dTheta
            
        value = abs(value) / (2 * pi)
        am.append(value)
            
    for indxM in range(ceil(N/2)):
        print('%d: %f' % (indxM, am[indxM]))
    
    print('Max Ratio %f' % (max / mid))
    print('Side-lobe max / side %f' % (max/side))
    print('hpbw %f' % (hpbw))
    print('hpbw2 %f' % (hpbw2))
    print('hpbw desired %f' % (pi / 8))
    
        

    plt.figure()
    plt.plot(x, sfFinal)
    
    
        
    
    
    plt.show()    
        
        
        