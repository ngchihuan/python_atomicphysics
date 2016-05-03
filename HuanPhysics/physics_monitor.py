# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:51:42 2015

@author: ngchihuan
"""
import numpy as np
class physics_monitor:
    #plotting a 2D array with a trimmed dataset
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