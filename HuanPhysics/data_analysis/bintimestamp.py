#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:39:15 2015

@author: ngchihuan
Timestamp binning module
"""
"""
DESCRIPTION:
Translate and binning timestamp file

INPUT:
filename: name of timestamp file
timebin: integration time in ms

OUTPUT:
trace[counts,channel]:
"""

#from __future__ import division # without this, python 2.x will understand 1/2 as 0.0
import numpy as np
import matplotlib.pyplot as plt
import argparse # parsing the args
import time
import sys

def binning(filename,timebin=10,partialbinning=[0,1]):


    binning=int((timebin)*10**-3/125*10**12)
    
    
    
    #Loading of data
    with open('%s' % filename, 'rb') as f:
        loaddata = np.fromfile(file=f, dtype='uint64')
    f.close()
    
    
    a=len(loaddata)
    if not partialbinning:
        begintrace=0
        endtrace=1
    else:
        begintrace=partialbinning[0]
        endtrace=partialbinning[1]
    
    
    #a rude way to handle exceptions
    if ((begintrace>endtrace) or (begintrace<0) or (endtrace>1) ):
        print ('errorbegintrace')
        sys.exit(0)
    
    ##################################################################
    
    loadingpointbegin=10 if (begintrace==0) else begintrace*a
    loadingpointend=-1 if (endtrace==1) else endtrace*a
    data=loaddata[loadingpointbegin:loadingpointend] # discard first 10 events
    cv = np.uint32((data << 32) >> 32) # coarse counter
    dv = np.uint32(data >> 32) # fine counter
    ######################################################################
    
    
    #MAIN PART###################################################################
    UPPERMASK  = 0x1fff000000000 #mask for identifying the 13 most significant bits in a 49 bit timing word
    # rollover every 19.5 hours: UPPERMASK * 125ps
    
    t_old=0
    delay=0
    rollovercorrection=0
    
    trace_start_time = ( cv[0] << 17 ) + ( dv[0] >> 15 ) - 1 # just before the first event
    trace_end_time = ( cv[-1] << 17 ) + ( dv[-1] >> 15 ) # just before the first event
    number_of_bins = int((trace_end_time- trace_start_time)/binning) + 1
    trace = np.zeros((number_of_bins,4)) # e.g. 20000 bins of 1 ms length
    print("total length of time trace: " + str(binning * number_of_bins * 125e-12) + " seconds")

    # main loop, go through every event
    for index in range(0,len(data)):
        t1 =  ( cv[index] << 17 ) + ( dv[index] >> 15 ) # time stamp of event
        pattern = dv[index] & 0xf # which detector-information
        ppat = ( dv[index] & 0x1ff0 )>>4 # some phase pattern shit
        # rollover 
        if(t1<t_old):
            if (((t1 & UPPERMASK)==0) and ((t_old & UPPERMASK)==UPPERMASK)):
                # correct rollover */
                rollovercorrection = rollovercorrection + (1<<49)
                t1 = t1 + (1<<49); # correct also current event */
                print("rollover!! new rollover:" + str(rollovercorrection) )
            else:
                print( "time reversal!! current event t1: " + str(t1) + ", previous event oldt1: " + str(t_old) )
        
        delay = t1 - t_old # time separation between events
        #print('t1: ' + str(t1) + '  pattern: ' + str(pattern) + '  ppat: ' + str(ppat) + '  delay: ' + str(delay) + '  delay (us): ' + str(125/1e6*delay))
        rel_t1 = t1 - trace_start_time # time stamp relativ to starting point
    
        timebin = int(rel_t1/binning) # this event belongs into bin 'timebin'
        trace[timebin,pattern-1] = trace[timebin,pattern-1] + 1
        t_old = t1
    
    return trace

