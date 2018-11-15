'''
Created on Nov 13, 2018

@author: dabrown
'''

from math import pi, cos, sqrt, log10
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pass
    
    d = 0.43
    beta = pi*d

    an = [1,0.7086,0.3447]


    af = []
    x = []
    for degree in range(0,720*2):
        theta = degree * pi / 720
        u = pi * d * cos(theta) - beta
        af.append(an[0] * cos(u) + an[1] * cos(3*u) + an[2] * cos(5*u))
        x.append(theta)
    
    
    # get hpbw for main lobe
    maxMain = af[0]
    indx = 0
    value = af[indx]
    while(value > maxMain / sqrt(2)):
        indx += 1
        value = af[indx]
        
    hpbw = 2*x[indx]
    
    maxBack = af[720]
    indx = 720
    value = af[indx]
    while(value > maxBack / sqrt(2)):
        indx += 1
        value = af[indx]
        
    hpbwBack = (x[indx] - pi)*2
    
    print('hpbw ', hpbw,'\nhpbwBack ', hpbwBack)
    
    
    
    
    af = af/np.max(af)
    af = abs(af)
    plt.figure()    
    plt.polar(x, af)
    plt.title('Figure 2: d = 0.43 y-z plane')
    plt.xlabel(r'$\theta$')
    plt.savefig('p1_second.png')
    
    x = np.multiply(x,180 / pi)
    plt.figure()
    plt.plot(x[0:720],af[0:720])
    plt.title('Figure 3: Array Factor y-z plane')
    plt.xlabel(r'$\theta$')
    plt.ylabel('AF')
    plt.savefig('p1_zeros.png')
    
    
    # get value of array factor at x-y plane
    value = af[360]
    x = np.linspace(0,2*pi,360)
    y = np.ones((360,1)) * value
    plt.figure()
    plt.polar(x,y)
    plt.title('Figure 4: AF for the x-y plane')
    plt.savefig('p1_xy.png')
    
    
    
    #sideLobeLevel = 
    maxSide = np.max(af[64*4:100*4])
    sll = 20*log10(maxSide/maxMain)
    
    print('sll ', sll)
    
    # mainBack ratio
    print('ratio ', maxMain/maxBack )
    
    
    
    
    
    
    
    
    
    plt.show()
    
    
    
    