# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:08:31 2015

@author: ngchihuan

Description: Standard Template for matplotlib plotting
"""

plt.figure(num=None, figsize=(20, 16), dpi=2000, facecolor='w', edgecolor='k')
plt.tick_params(axis='x', labelsize=30)
plt.tick_params(axis='y', labelsize=30)
plt.title('Transmission(10ms timebin)',fontsize=25)
plt.xlabel('Time',fontsize=25)
plt.ylabel('Tranmission',fontsize=25)
d1=da217.a1[:,1]-500
d2=da217.a2[:,1]-500
plt.plot(d1,label='with MOT')
plt.plot(d2,label='without MOT')
plt.legend(loc='upper right',prop={'size':20})
plt.savefig("tr3")