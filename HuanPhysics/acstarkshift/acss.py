# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:50:05 2015

@author: ngchihuan

How to use:

Import: from HuanPhysics.ACStarkShift import acss

EshiftS(F1,mF1,q,J1,w,I0)
Calculate the ACStarkShift of 5S1/2 states
F1,mF1: 5S1/2 states
q: Polarization of trapping beam, (-1,0,+1)=(left,linear,right)
J1:1/2
I0:peak intensity of trapping beam
w: wavelength of trapping beam
Similarly for EshiftP

resShift(F1,mF1,J1,F2,mF2,J2,q,w,I0):
#The AC shift from the resonant transition between |F1,mF1,J1> and |F2,mF2,J2>

plotwaist: plot acs as a function of waist of trapping beam
"""
from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
from . import wigner as wg
import numpy as np
from scipy import constants as c
from sympy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from decimal import * #to control the decimal
from imp import reload
reload(wg)
getcontext().prec = 7 
import gc
gc.collect()
lsp=2.998*10**8
kbt=1.3806488*10**-23
global I1 
I1=3/2#nuclear spin 
global re1

#Supporting Functions
def PowertoInten(waist,power):
    inten=2*power/3.14/(waist**2)
    return inten
PowertoInten(1*10**-6,0.04)

#Datasheet
def datasheet(x): #datasheet including resonant freq and 1/lifetime of Rb transition
    global re
    re=0
    if x==([5,1,1/2]):
        re=[2*c.pi*lsp/(7949.783*10**-10),3.592*10**7]
    if x==([5,1,3/2]):
        re=[2*c.pi*lsp/(7802.405*10**-10),3.755*10**7]
    if x==([6,1,1/2]):
        re=[2*c.pi*lsp/(4216.706*10**-10),2.456*10**6]
    if x==([6,1,3/2]):
        re=[2*c.pi*lsp/(4202.972*10**-10),3.664*10**6]
    if x==([7,1,1/2]):
        re=[2*c.pi*lsp/(3592.593*10**-10),7.266*10**5]
    if x==([7,1,3/2]):
        re=[2*c.pi*lsp/(3588.070*10**-10),1.266*10**6]
    return re
    
def Coef(F1,F2,mF1,mF2,q,J1,J2):
    result=np.power(-1,(J1+I1+mF1))*np.sqrt((2*J1+1)*(2*F2+1)) \
    *wg.ClebschGordan(F2,1,mF2,q,F1,mF1)*wg.Wigner6j(J1,J2,1,F2,F1,I1)
    return (result**2)

def delJJ(w0,w):
    re=1/(w0+w)
    return re
def delJJN(w0,w):
    re=1/(w0-w)
    return re
    
    
    
#the shifting of groundstate (5S1/2) F1 mF1 due to state n2,L2,J2 with I0 intensity at frequency w
###############################################
#Input parameters:
#w: angular freq of laser beam
#I0 is the intensity of laser beam
#q: polarization of laser beam(only receive +-1 and 0; 0 is for linear polarization)
################################################
#Output: AC Shift in (J) of #the shifting of groundstate (5S1/2) F1 mF1 due to state n2,L2,J2 with I0 intensity at frequency w
##################################################
def shiftSJJ(n2,L2,J2,J1,F1,mF1,q,w,I0):
    F2=np.abs(J2-I1)
    v1=0
    while F2<(J2+J1+1):
        mF2=-F2
        while mF2<(F2+1):
            v1=v1+Coef(F1,F2,mF1,mF2,q,J1,J2)
            mF2=mF2+1;
        F2=F2+1
    v2=0
    F2=np.abs(J2-I1)
    while F2<(J2+J1+1):
        mF2=-F2
        while mF2<(F2+1):
            v2=v2+Coef(F1,F2,mF1,mF2,-q,J1,J2)
            mF2=mF2+1;
        F2=F2+1
    v3=3*c.pi*(2.998*10**8)**2*I0*datasheet([n2,L2,J2])[1]*(v1*delJJ(-datasheet([n2,L2,J2])[0],w)\
      +v2*delJJN(-datasheet([n2,L2,J2])[0],w))/(2*np.abs(datasheet([n2,L2,J2])[0])**3)
    v=v3*(2*J2+1)/(2*J1+1)
    return v
shiftSJJ(5,1,3/2,1/2,2,2,-1,980**(-9),1)
        
#Total AC Stark Shift of state F1,mF1
def EshiftS(F1,mF1,q,J1,w,I0):
    re=shiftSJJ(5,1,1/2,J1,F1,mF1,q,w,I0)\
    +shiftSJJ(5,1,3/2,J1,F1,mF1,q,w,I0)\
    +shiftSJJ(6,1,1/2,J1,F1,mF1,q,w,I0)\
    +shiftSJJ(6,1,3/2,J1,F1,mF1,q,w,I0)\
    +shiftSJJ(6,1,1/2,J1,F1,mF1,q,w,I0)\
    +shiftSJJ(6,1,3/2,J1,F1,mF1,q,w,I0)
    return re
   

def datasheet2(x): #datasheet including resonant freq and 1/lifetime of Rb transition from 5P3/2
    global re
    re=0
    if x==([5,0,1/2]):
        re=[2*c.pi*lsp/(-7800.259*10**-10),3.755*10**7]
    if x==([6,0,1/2]):
        re=[2*c.pi*lsp/(13666.2993*10**-10),1.311*10**7]
    if x==([7,0,1/2]):
        re=[2*c.pi*lsp/(7408.166*10**-10),0.44*10**6]
    if x==([8,0,1/2]):
        re=[2*c.pi*lsp/(6159.619*10**-10),2.192*10**6]
    if x==([4,2,3/2]):
        re=[2*c.pi*lsp/(15288.938*10**-10),0.208*10**7]
    if x==([4,2,5/2]):
        re=[2*c.pi*lsp/(15289.966*10**-10),1.25*10**7]
    if x==([5,2,3/2]):
        re=[2*c.pi*lsp/(7759.429*10**-10), 4.788*10**5]
    if x==([5,2,5/2]):
        re=[2*c.pi*lsp/(7757.647*10**-10),2.7*10**6]
    if x==([6,2,3/2]):
        re=[2*c.pi*lsp/(6299.221*10**-10),5.3*10**5]
    if x==([6,2,5/2]):
        re=[2*c.pi*lsp/(6298.324*10**-10),3.16*10**6]
    return re
def shift2(n2,L2,J2,J1,F1,mF1,q,w,I0):
    F2=np.abs(J2-I1)
    v1=0
    while F2<(J2+J1+1):
        mF2=-F2
        while mF2<(F2+1):
            v1=v1+Coef(F1,F2,mF1,mF2,q,J1,J2)
            mF2=mF2+1;
        F2=F2+1
    v2=0
    F2=np.abs(J2-I1)
    while F2<(J2+J1+1):
        mF2=-F2
        while mF2<(F2+1):
            v2=v2+Coef(F1,F2,mF1,mF2,-q,J1,J2)
            mF2=mF2+1;
        F2=F2+1
    v3=3*c.pi*(2.998*10**8)**2*I0*datasheet2([n2,L2,J2])[1]*(v1*delJJ(-datasheet2([n2,L2,J2])[0],w)\
      +v2*delJJN(-datasheet2([n2,L2,J2])[0],w))/(2*np.abs(datasheet2([n2,L2,J2])[0])**3)
    v=v3
    if (datasheet2([n2,L2,J2])[0]>0):
        v=v3*(2*J2+1)/(2*J1+1)
    return v

#Total AC Stark Shift of 5P3/2 state
def EshiftP(F1,mF1,q,J1,w,I0):
    re=shift2(5,0,1/2,J1,F1,mF1,q,w,I0)\
    +shift2(6,0,1/2,J1,F1,mF1,q,w,I0)\
    +shift2(7,0,1/2,J1,F1,mF1,q,w,I0)\
    +shift2(4,2,3/2,J1,F1,mF1,q,w,I0)\
    +shift2(4,2,5/2,J1,F1,mF1,q,w,I0)\
    +shift2(5,2,3/2,J1,F1,mF1,q,w,I0)\
    +shift2(5,2,5/2,J1,F1,mF1,q,w,I0)
    return re

#The AC shift from the resonant transition between |F1,mF1,J1> and |F2,mF2,J2>
def resShift(F1,mF1,J1,F2,mF2,J2,q,w,I0):
    re=EshiftP(F2,mF2,q,J2,w,I0)-EshiftS(F1,mF1,q,J1,w,I0)
    return re


#Demo plotting
def plotwaist(F1,mF1,q,J1,w=2*3.14*2.998*10**17/810,p_intra=20*10**-3, waist=np.arange(1*10**-6,20*10**-6,0.5*10**-6)):
   
    a=len(waist)    
    inten=np.ones((a,2))
    acshift=np.ones((a,2))
    for i in range(a):
        inten[i]=PowertoInten(waist[i],p_intra)
        acshift[i]=EshiftS(F1,mF1,q,J1,w,inten[i])/c.h/10**6
    
    axis_font = {'fontname':'Arial', 'size':'350'}
    plt.figure(num=None, figsize=(20, 16), dpi=1000, facecolor='w', edgecolor='k')
    plt.tick_params(axis='both', which='major', labelsize=25)
    plt.title('ACShift of ground state(Trap depth) with Intracav Power '+str(p_intra*10**3) +'mW',fontsize="30")
    plt.xticks(np.arange(min(waist*10**6), max(waist*10**6)+1, 1.0))
    plt.xlabel('waist(um)',fontsize="30")
    plt.ylabel('ACshift',fontsize="30")
    plot1=plt.plot(waist*10**6,acshift, marker='o', linestyle='--', color='r', label='Square')
    return plot1
if __name__=='__main__':
    plotwaist(2,2,0,1/2,2*3.14*2.998*10**17/810,1)
