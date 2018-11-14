'''
Created on Nov 13, 2018

@author: dabrown
'''

import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin

if __name__ == '__main__':
    pass


    # xz plane
    phi = 0
    
    thetas = np.linspace(0,2*pi,720)
    afXz = []
    for theta in thetas:
        psiX = pi * sin(theta) * cos(phi)
        psiY = pi * sin(theta) * sin(phi)
        psiZ = pi * cos(theta) - pi
        afx = (1+cos(psiX))
        afy = (1+cos(psiY))
        if( abs( 2*sin(psiZ/2)) > 0):
            afz = sin(psiZ) / ( 2*sin(psiZ/2) )
        else:
            afz = 1
                              
        ef = abs(cos(theta) * sin(phi) + cos(phi))                  
        af =  afx * afy * afz * ef
        afXz.append(af)
    
    afXz = afXz / np.max(afXz)
    plt.figure()
    plt.polar(thetas, afXz)
    plt.title('AF along X-Z plane')
    plt.xlabel(r'$\theta$')
    plt.savefig('prob2_xz.png')
    
    # yz plane
    phi = pi/2
    
    thetas = np.linspace(0,2*pi,720)
    afYz = []
    for theta in thetas:
        psiX = pi * sin(theta) * cos(phi)
        psiY = pi * sin(theta) * sin(phi)
        psiZ = pi * cos(theta) - pi
        afx = (1+cos(psiX))
        afy = (1+cos(psiY))
        if( abs( 2*sin(psiZ/2)) > 0):
            afz = sin(psiZ) / ( 2*sin(psiZ/2) )
        else:
            afz = 1

        ef = abs(cos(theta) * sin(phi) + cos(phi))                     
        af =  afx * afy * afz * ef
        afYz.append(af)
    
    afYz = afYz / np.max(afYz)
    plt.figure()
    plt.polar(thetas, afYz)
    plt.title('AF along Y-Z plane')
    plt.xlabel(r'$\theta$')
    plt.savefig('prob2_yz.png')

    
    plt.show()
    
    
    