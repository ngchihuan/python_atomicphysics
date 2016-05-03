# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:17:02 2016

@author: ngchihuan
OOP STARK SHIFT FLEXIBLE SCHEME
IMPLEMENT ACSTARK SHIFT CALCULATION WITH STRATEGY PATTERNS TO FLEXILIBLY 
INCLUDE DIFFERENT ALGORITHMS 
"""
import math as m
class atom():
    def __init__(self,I=3/2):
        self.states=[]
        self.I=I
    def add_state(self,L):
        #add states, input J or F or L
        pass
    def find_sibling(self,L):
        J=abs(L-1/2)
        while (J<=(L+1/2)):
            F=abs(J-self.I)
            while (F<=(J+self.I)):
                mF=-F
                while(mF<=F):
                    qnumber=[0,L,J,F,mF]
                    self.states.append(state(qnumber=qnumber))
                    mF=mF+1
                F=F+1
            J=J+1
        
class state():
    #public: J,F,mF, take J or F as input and automatically generate the siblings
    def __init__(self,qnumber=[0,0,0,0,0,0]):
        #should include @property
        self.qnumber=qnumber
        self.energy=0

if __name__=="__main__":
    atom1=atom()
    atom1.find_sibling(L=0)
    l=len(atom1.states)
    print(l)
    for i in range(l):
        print(atom1.states[i].qnumber)
    
    
    
