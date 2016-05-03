# -*- coding: utf-8 -*-
from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
"""
Created on Wed Aug 12 13:59:19 2015

@author: ngchihuan
Ei returns array of energy of eigenstates of quantum harmonic oscillators
with input n-number of states and w-trap frequency
Ereal does a similar job. In addition Ereal cut off the number of states with energy
below the trap depth
"""


import numpy as np
import scipy as sci
import math
from scipy import constants
from decimal import * #to control the decimal
getcontext().prec = 7 
k=sci.constants.k
h=sci.constants.h
hbar=sci.constants.hbar

def Ei(n,w):
    #w is the trap frequency
    #Calculate energy of state n in the trap
    Ei=np.zeros(n)
    for i in range(0,len(Ei)):
        Ei[i]=hbar*w*(i+1/2)
    return Ei
    
def Ereal(n,w,U):
    #U is the trap depth in Energy
    #recommend to set n high enough
    Eiw=np.zeros(n)
    Eiw=Ei(n,w)
    n=np.size(Ei)
    E=[]
    for i in range(0,len(Eiw)):
        if (Eiw[i]<U):
            E.append(Eiw[i])
        else:
            break
    return E
            
            
    