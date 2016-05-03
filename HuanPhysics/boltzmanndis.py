# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:55:43 2015

@author: ngchihuan
Prob_state_arr returns the Boltzmann probability distribution with input of energy array

"""
from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
import numpy as np
import scipy as sci
from scipy import constants
from decimal import * #to control the decimal
getcontext().prec = 7 
k=sci.constants.k
import harmonictrap

def Prob_state(Ei,T):
    p=np.exp(-Ei/(k*T))
    return p

def Prob_state_arr(E,T):
    #Ei is an array of energy of states
    n=np.size(E)
    p=np.zeros(n)
    for i in range(0,len(E)):
        p[i]=(np.exp(-E[i]/(k*T)))
    sump=np.sum(p)
    pnorm=p/sump
    return pnorm

if __name__ == "__main__":
    import sys
    #parsing a1 a2
    #a1 is Ei,a2 is T
    Ei=harmonictrap.Ei(50,300*10**3)
    T=float(sys.argv[2])
    b=Prob_state(float(sys.argv[1]),T)
    p=Prob_state_arr(Ei,T)
    print (b)
