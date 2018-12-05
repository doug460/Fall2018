'''
Created on Dec 4, 2018

@author: DougBrownWin
'''

import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    pass

    data = np.loadtxt('dB_MagAndPhase2_5GHz.txt')
    
    firstPoint = data[0][0]
    
    indx = 1
    while data[indx][0] != firstPoint:
        indx += 1
        
    indx -= 1
    
    
    degrees = data[0:indx, 0]
    dbs     = data[0:indx, 2]
    
    plt.plot(degrees, dbs)
    plt.title('Gain (dB) at 2.5 GHz')
    plt.xlabel('degrees')
    plt.ylabel('Gain (dB)')
    plt.savefig('2.5 GHz dB.png')
    plt.show()