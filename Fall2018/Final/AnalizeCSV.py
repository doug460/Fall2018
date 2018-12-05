'''
Created on Dec 4, 2018

@author: DougBrownWin
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    pass

    data = np.loadtxt('S11.CSV', delimiter = ',' ,skiprows = 3)
    
    x = data[:,0]
    y = data[:,1]
    
    plt.plot(x,y)
    plt.title('Reflection (S11)')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('S11')
    plt.savefig('reflection.png')
    plt.show()