# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:57:14 2015

@author: ngchihuan
Optical resonator calculations
"""
from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
import numpy as np
from scipy import constants as const
c=const.speed_of_light
ep=const.epsilon_0
hbar=const.hbar
pi=const.pi
def w0(R1,R2,L,lamda):
    """
    minimum beam waist
    w0(R1,R2,L,lamda)
    R1,R2: ROC of mirror 1 and mirro2
    L: length of cavity
    lamda: wavelength of input beam
    """
    g1=(1-L/R1)
    g2=1-L/R2
    w01=(L*lamda/pi)**(1/2)*(g1*g2*(1-g1*g2)/(g1+g2-2*g1*g2)**2)**(1/4)
    return w01
def wm(R,L,lamda):
    wm=np.sqrt((lamda*R/pi)/np.sqrt(2*R/L-1))
    return wm
def wz(R1,R2,L,lamda,z):
    '''
    beam waist at position z
    wz(R1,R2,L,lamda,z)
    R1,R2: ROC of mirror 1 and mirro2
    L: length of cavity
    lamda: wavelength of input beam
    z: position z
    '''
    wz=(w0(R1,R2,L,lamda)**2*(1+(z/zr(R1,R2,L,lamda))**2))**(1/2)
    return wz
def zr(R1,R2,L,lamda):
    '''
    Rayleigh range
    zr(R1,R2,L,lamda)
    R1,R2: ROC of mirror 1 and mirro2
    L: length of cavity
    lamda: wavelength of input beam
    
    '''
    zr=pi*w0(R1,R2,L,lamda)**2/lamda
    return zr
def tmp(R,L,lamda):
    g=1-L/R
    #res=sol/(2*L)*[1+np.cos(L)]
    res=sol/(2*L)*(1/pi*np.arccos(g)-1)
    return res
#Mode volume
def mode_volume(R,L,wavelength):
    '''
    mode_volume (assume uniform distribution?)
    mode_volume(R,L,wavelength):
    '''
    Vm = (wavelength/8)*np.sqrt(2*R*L**3-L**4)
    return Vm
def cavity_mode_matching(w1,w2,R2,lamda):
    """
    collimated beam q1 ->thin lens->free space propagation->q2(w2,R2)
    cavity_mode_matching(w1,w2,R2,lamda):
    w1,w2 beam waist of q1 q2
    R2 ROC of q2
    """
    b=lamda/pi/w1**2
    d=lamda/pi/w2**2
    rangef=10**-3*np.arange(30,500,10)
    print("lens focus \t length")
    for f in rangef:
        x=1/f
        z=(b/d/R2+x)/(x**2+b**2)
        
        print(f,z)
if __name__=='__main__':
    #Testing cases for cavity beam waist
    L=2e-2
    R1=50e-3
    R2=R1
    R=R2
    lamda=780e-9
    #waist at center:0.59e-3; at mirror: 0.61e-3
    w2=wm(R,L,lamda)
    #print( w0(R1,R2,L,lamda),wm(R,L,lamda),wz(R1,R2,L,lamda,L/2),wz(R1,R2,L,lamda,0),zr(R1,R2,L,lamda))
    print (w2)
    cavity_mode_matching(1.1e-3,w2,R1,lamda)
    
    
    