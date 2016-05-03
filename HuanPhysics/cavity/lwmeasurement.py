# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:18:32 2015

@author: ngchihuan
"""
#may extend lwmeasurement as a subclass of a superclass measurement which can be used
#as an interface for all measurements
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import leastsq
import pylab as P
from HuanPhysics import physics_monitor
class lwmeasurement:
    #class variables
    #
    #probably need to have 2 constructors to allow file input or dataset input
    def __init__(self,dataset):
        self.dataset=dataset
        self.x=dataset[:,0]
        self.y=dataset[:,1]
        pass

    #Plants
    def getcalibration(self):
        pass
        
    #monitor
    def getlw(self):
        pass
    def getfit(self):
        pass
    #probably implement a generic interface for monitor/plot/display in the superclass measurement in the future
    #display can be packed into another class or module
    def display(self,xlabel='',ylabel=''):
        self.xlabel=xlabel
        self.ylabel=ylabel
        plt.figure(num=None, figsize=(10, 8), dpi=1000, facecolor='w', edgecolor='k')
        plt.title('Cavity 810nm Transmission')
        #not yet implement xlabel with variables
        plt.xlabel(str(self.xlabel))
        plt.ylabel(self.ylabel)
        #for dumb in trimrange:
        #    self.trimrange.append(dumb)
        #need to raise exception for trimrange must be less than 2 numbers and in the increasing order
        #
        #self.x=self.dataset[(lambda
        self.plot1=P.plot(self.x,self.y)
 
    def getmax(dataset,trimrange):
        datasettemp=lwmeasurement.trim(dataset,trimrange)
        maxtemp=np.argmax(datasettemp[:,1])
        return maxtemp
   
    def __rep__(self):#overloading 
        #displaying graph by using display when callers use print(object)    
        pass
    #pickling or shelving python objects into database
    def savepickle(self):
        pass
    def saveshelv(self):
        pass
    def trim(dataset=[],trimrange=[]):
        if not (trimrange):
            x=dataset[:,0]
            y=dataset[:,1]
        else:
            x=dataset[trimrange[0]:trimrange[1],0]
            y=dataset[trimrange[0]:trimrange[1],1]     
        res=np.transpose(np.vstack((x,y)))
        return res
def getmax2(dataset,initx=0,step=150,tol=10):
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
def display(dataset=[],trimrange=[],xlabel='',ylabel='',numdisplay=False):
        xlabel=xlabel
        ylabel=ylabel
        plt.figure(num=None, figsize=(10, 8), dpi=1000, facecolor='w', edgecolor='k')
        plt.title('Cavity 810nm Transmission')
        #not yet implement xlabel with variables
        plt.xlabel(str(xlabel))
        plt.ylabel(ylabel)
        trimrange=trimrange
        #for dumb in trimrange:
        #    self.trimrange.append(dumb)
        #need to raise exception for trimrange must be less than 2 numbers and in the increasing order
        #
        if not (trimrange):
            x=dataset[:,0]
            y=dataset[:,1]
        else:
            x=dataset[trimrange[0]:trimrange[1],0]
            y=dataset[trimrange[0]:trimrange[1],1]           
        #self.x=self.dataset[(lambda
        if not numdisplay :
            plot1=P.plot(x,y)
        else:
            xnum=np.arange(0,np.size(x),1)
            plot1=P.plot(xnum,y)
if __name__=='__main__':
       
        dataset100sb = np.genfromtxt("/home/ngchihuan/ngchihuan@gmail.com/Research/Exp_Data/Cavity/Tranmission/2015-10-6/810transmission2015_10_6/C2100mhzsideband00000.txt",skip_header=5)
        trimrange=[9500,12000]
        # lw1.display(trimrange,xlabel='dsh',ylabel='ewytwy')
        dataset=lwmeasurement.trim(dataset100sb,trimrange)
        lw1=lwmeasurement(dataset)
        lw1.display();
        #print (np.shape(datasettrim))
        a1=1000
        a2=1500
        trimrange1=[a1,a2]
        display(lw1.dataset,trimrange=[],numdisplay=True)
        print (np.shape(dataset))
        res=getmax2(dataset,initx=0)
        for x in res:
            print (dataset[x])
        print (np.max(dataset[:,1]))
        #physics_monitor.display(dataset100sb,trimrange,xlabel='dsh',ylabel='ewytwy')
       
       

    
        
        