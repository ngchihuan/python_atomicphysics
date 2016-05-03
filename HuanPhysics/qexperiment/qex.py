# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:25:18 2016

@author: ngchihuan
front-end interface
as a part of qexperiment project
ONLY WORK FOR 1 LAYER NOW
"""
import measurement_params as mp
import q_database as qdb
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import shelve
class qex():
#for parent node
    def __init__(self,mainpath,name="default",function=None):
        #db is database
        #self.db=qdb.qdb(mainpath,name)
        self.paramslist=mp.measurement_params()
        self.info={}
        for i in self.paramslist.list_params:
            self.info[i]=[]
        if check_existed(mainpath,name):
            self.load(name,mainpath)
            
        else:
            self.init(mainpath,name,function)
        
#######################################
#interface to users function
#######################################  
    def init(self,mainpath,name,function):
        print("Initiating new measurement")
        self.paramslist=mp.measurement_params()
        self.info={}
        for i in self.paramslist.list_params:
            self.info[i]=[]
        self.info['name'].append(name)
        self.info['function'].append(function)
        self.info['mainpath'].append(mainpath)
        self.mainpath=mainpath
        self.name=name
    def add_dbinfo(self,*extra_params):
        self.params.add(extra_params)
    

    def add_function(self,function):
        '''
        add function to process tha data
        '''
        self.function=function
        pass
    
    def on_analysis(self,verbose=False):
        if self.info['function']==None:
            print("Error: havent added function")
        self.on_analysis_mech()
       

    def save(self):
        '''
        save results
        '''
        self.s=self.info['mainpath'][0]+'/'+self.info['name'][0]
        self.db=shelve.open(self.s)
        for i in self.info:
            self.db[i]=self.info[i]
        self.db.close()
    
    def get(self,attri):
        return self.info[attri]
    def load(self,name,mainpath):
        '''
        load results
        '''
        print("Loading database %s" %name)
        self.s=mainpath+'/'+name
        self.db=shelve.open(self.s)
        for i in self.info:
            self.info[i]=self.db[i]
        self.db.close()
        
    
    def display(self):
        pass
    
    def on_analysis_mech(self,function=None,param_to_save='data'):
        tarpath=self.info['mainpath'][0]
        function=self.info['function'][0]
        folderlist=[f for f in listdir(tarpath) if os.path.isdir(join(tarpath, f))]
        for folder in folderlist[0:2]:
            tarpath2=tarpath+'/'+folder
            q=qex(tarpath2,function=function)
            
            filelist=[f for f in listdir(tarpath2) if os.path.isfile(join(tarpath2, f))]
            for f in filelist[0:1]:
                filepath=tarpath2+'/'+f
                #print(filepath)
                fileName,fileExtension = os.path.splitext(filepath)
                if fileExtension==".txt":
                    result=analyze(function,filepath)
                q.info['data'].append(result)
            self.info[param_to_save].append(q) 
            print("#################")
###########################################    
class qex_sub(qex):
    #to deal with subnode 
    pass

   
###########################################
#Hidden functions to process
###########################################        
def check_existed(mainpath,name):
    #checked if there existed a database with the input name
    filelist=[f for f in listdir(mainpath) if os.path.isfile(join(mainpath, f))]
    return (name in filelist)
        
    
    
def analyze(function,filepath):
    #NEED TO ADD EXCEPTION TO LOG INTO DATABASE IN ON_ANALYSIS_MECH
    data=np.genfromtxt(filepath,skip_header=5)
    result=function(data)
    #print(result)
    return result
    
    #dumpdatabse(qex)
    #save result into database
def dumpdatabase(qex):
    db=shelve.open(qexname)
     
    
    
def tree_directory(tarpath):
        #return a nested dictionary containing information about directories in the mainpath
        parent_name=os.path.basename(os.path.normpath(tarpath))
        dic={}
        dic[parent_name]={}
        folderlist=[f for f in listdir(tarpath) if os.path.isdir(join(tarpath, f))]
        for f in folderlist:
            dic[parent_name][f]={}
            tarpath2=tarpath+'/'+f
            folderlist2=[f2 for f2 in listdir(tarpath2) if os.path.isdir(join(tarpath2, f2))]
            for f2 in folderlist2:
                dic[parent_name][f]=f2
        return dic
def print_dic(dic):
    #print nested dic
    for k in dic:
     
        if type(dic[k])==dict:
            print_dic(dic[k])
        else:
            print('\t'+dic[k])
            
if __name__=="__main__":
    tarpath="/home/ngchihuan/research/exp_data/Cavity/2nd_set/2015_12_31"
    dic=tree_directory(tarpath)
    
    def f(a):
        return 1
    q1=qex(tarpath,name="d2",function=f)
    q1.on_analysis()
    
    
    
        
