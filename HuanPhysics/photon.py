# -*- coding: utf-8 -*-
from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
"""
Created on Thu Aug 20 11:19:02 2015

@author: ngchihuan
This python module provides some basic calculations in photonics
"""


import numpy as np
from scipy import constants as c
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from decimal import * #to control the decimal
import math
getcontext().prec = 7 

lsp=2.998*10**8
kbt=1.3806488*10**-23
h=6.62606957*10**-34

def Ephoton(wavelength):
    Energy=h*lsp/wavelength
    return Energy
    
def Power_Number(power,wavelength):
    """
    Power_Number(power,wavelength)
    """
    photonNumber=power/Ephoton(wavelength)
    return photonNumber
    
def Number_Power(number,wavelength):
    power=number*Ephoton(wavelength)
    return power

def Power_Intensity(power,waist):
    Intensity=power*2/3.14/(waist**2)
    return Intensity

def Intensity_Power(intensity,waist):
    power=intensity/2*3.14*(waist**2)
    return power
    
def zR(waist,lamda):
    zr=math.pi*(waist**2)/(lamda)
    return zr
