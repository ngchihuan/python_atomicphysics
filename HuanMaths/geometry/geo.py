# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:06:50 2015

@author: ngchihuan
"""
import numpy as np
class GeoObject():
    def sphere(center,radius):
		N=72
		phi = np.linspace(0.0,2.0*np.pi,N)
		x = np.cos(phi)*radius
		y = np.sin(phi)*radius
		
		xy = []
		for (a,b) in zip(x,y):
			xy.append([a,b])
       print x
   return xy