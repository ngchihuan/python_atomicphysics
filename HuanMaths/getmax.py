# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:19:22 2015

@author: ngchihuan
"""

def getmax(dataset,initx=0,step=150,tol=10):
#second method to automatically get peak by slowly move up the hills
    initx=initx
    end_x=initx+step
    maxpo=[]
    print (np.size(dataset,0))
    x=dataset[initx:end_x,0]
    y=dataset[initx:end_x,1]
    while ((initx+step)<np.size(dataset,0)):
        print(initx,end_x)
        x=dataset[initx:end_x,0]
        y=dataset[initx:end_x,1]
        t1=np.size(x)
        maxy=np.argmax(y)
        print(maxy)
        if (maxy>(t1-tol)) or (maxy<tol):
            pass
        else :
            maxpo.append(maxy+initx)
        initx=end_x
        end_x=end_x+step
    return maxpo