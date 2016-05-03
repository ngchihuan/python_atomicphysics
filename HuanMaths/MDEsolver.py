# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:29:22 2015

@author: ngchihuan
"""

from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def deriv(P, t, A):
    return np.dot(A, P)

def MDEsolver(nstate,P0,Gam)
nstate=50
state=np.linspace(0,nstate-1,nstate)
print state
A=np.zeros((nstate,nstate))
for n in range(0,len(A)):
    A[n,n]=-(n*(n-1)+(n+2)*(n+1))
    if ((n+2)<len(A)):
        A[n,n+2]=(n+2)*(n+1)
    if ((n-2)>=0):
        A[n,n-2]=n*(n-1)
#S=1*10**-9
#trapfreq=300*10*6
#bwd is bandwidth of photodetector
#Gam=3.14**2*trapfreq**2*S
A=Gam/8*A

P0=np.zeros(nstate)
for n in range(0,len(P0)):
    P0[10]=1
    
def deriv(P, t, A):
    return np.dot(A, P)
t=np.linspace(0,0.01,200)
MA = odeint(deriv, P0, t, args=(A,), mxstep=200,printmessg=1)

x,y=np.meshgrid(state, t)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, MA, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
plt.show()