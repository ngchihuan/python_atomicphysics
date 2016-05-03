# -*- coding: utf-8 -*-
from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
"""
Created on Sun Aug 16 14:54:27 2015

@author: ngchihuan
#Nguyen Chi Huan
#Calculation of Freq for Dipole beam
#To determine freq of dipole beam to be on resonance with cavity that is on resonance with probe beam
#Can also be used to determine the actual length of the cavity based on the frequency of 2 beams on
#on resonance with the cavity at the same time
"""
#%matplotlib inline
import numpy as np
from scipy import constants as c
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from decimal import * #to control the decimal
getcontext().prec = 7 
lsp=299792458#speed of light
def predict_length(deltaLstart,deltaLend,L,laser1wl,laser2wl):
        L1=L-deltaLstart
        L2=L-deltaLend
        a1=round(L1*2/laser1wl)
        a2=round(L2*2/laser1wl)
        da=np.abs(a2-a1+1)
        Lpo=np.ones((da,1))#possible length of cavity
        lamdapossible=np.ones((da,1)) #Possible wavelength for 810 to be on co-resonant with lamda21 on the the cavity
        rt=np.ones((da,1))
        
        for i in range(0,len(Lpo)-1):
            Lpo[i]=(a2+i)/2*laser1wl
 
            rt[i]=round(Lpo[i]*2/laser2wl)
            lamdapossible[i]=Lpo[i]*2/rt[i]
  
        wlpossible=lsp/lamdapossible
        errwl=np.abs(wlpossible-laser2wl)
        position_minwl=np.argmin(errwl)
        errmin=errwl[position_minwl]
        dtype=[('wlpossible',float),('lengthpossible',float),('error',float)]
        print np.shape(wlpossible)
        value=[wlpossible,Lpo,errwl]
        a=np.array(value,dtype=dtype)
     
        return a
        
class cavitylength:
    lsp=299792458#speed of light
    def __init__(self,laser1f,laser2f,L,deltaLstart,deltaLend):
        self.laser1f=laser1f
        self.laser2f=laser2f
        self.laser1wl=lsp/self.laser1f
        self.laser2wl=lsp/self.laser2f
        self.L=L#length of cavity
        self.deltaLstart=deltaLstart
        self.deltaLend=deltaLend
        self.result=[]
    def predict(self):
        a=predict_length(self.deltaLstart,self.deltaLend,self.L,self.laser1wl,self.laser2wl)
        self.result.append(a)
        
        
        
        
        
   
    
   
        
        
        
    