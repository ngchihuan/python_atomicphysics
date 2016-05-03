# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:21:11 2015

@author: ngchihuan
a class to store reference of parameters that can be saved into database
as a part of qexperiment project
must have an ability to add more optional parameters
"""

class measurement_params():
    def __init__(self):
        self.list_params=['number_data_point','data','data_mean','data_std',
        'last_accessed','data_flag','description','function','name','mainpath']
    def add(self,*extra_params):
        for i in extra_params:
            if not (i in self.list_params):
                self.list_params.append(i)
if __name__=="__main__":
    a= measurement_params()
    a.add('wet')
    a.add('qwe','werwe')
    print(a.list_params)
    