# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:48:11 2015

@author: ngchihuan
"""

import numpy as np
from scipy import constants as const
c=const.speed_of_light
ep=const.epsilon_0
hbar=const.hbar

def rabifreq(I,d12=2.5342707037725868e-29):
    rabi=d12/hbar*np.sqrt(2*I/c/ep)
    return rabi

def I_from_rabifreq(rabi,d12=2.5342707037725868e-29):
    I=((rabi*hbar/d12)**2)*c*ep/2
    return I

def I_sat(decayrate=2*3.14*6.065*10**6,d12=2.5342707037725868e-29):
    I_sat=c*ep*decayrate**2*hbar**2 /4/(d12**2)
    return I_sat
    
def Rsc(I,detunning=0,decayrate=2*3.14*6.065*10**6,d12=2.5342707037725868e-29):
#detuning in angular freq
    I_sat=I_sat(decayrate,d12)
    Ibar=I/I_sat
    Rsc=decayrate/2*Ibar/(1+Ibar+4*detunning**2/decayrate**2)
    return Rsc
    
#coupling strength,rabifreq in quantization mode
def coupling_strength(Vm,lamda,decayrate):
    """
    Calculate coupling_strength atom and quantitized mode in angular freq

    Another version is coupling_strength2
    
    Args:
    Vm: Mode volume
    lamda: wavelength
    decayrate: 1/radiative lifetime 2pi6.065MHz for D2 Rb2
    """
    g0 = np.sqrt(3*lamda**2*c*decayrate/(4*np.pi*Vm))
    return g0

def coupling_strength2(Vm,w,d12):
    """
    Calculate coupling_strength atom and quantitized mode in angular freq
    
    Args:
    
    Vm: Mode volume
    w: wavelength
    d12:dipole strength
    """
    g0=d12*np.sqrt(w/(2*ep*Vm*hbar))
    return g0
    
if __name__=='__main__':
    print("Testing for Rb87 D2 5S1/2->5P3/2 F=2,mF=2->F=3,mF=3")
    print(rabifreq(I=2*1.69*10))
    print(I_from_rabifreq(rabi=38156128))
    print(I_sat())
