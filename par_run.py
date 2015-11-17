# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 11:42:03 2011

@author: Jelle Langmans
"""


from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from  numpy.random import randn
import  numpy.random as random
from pandas import Series, DataFrame
import math
import sys,os
direct_sim='C:/Users/jelle/Dropbox/phyb/PYTHON'  #'C:/JELLE' #'C:/PostDoc/SIMULATIES'
sys.path.append(direct_sim)
from definities import *
# laat toe om alle functie en classes die gedefinieerd zijn te gebruiken




#BASEFILE 
base_dir = direct_sim+'/voorbeeld_input.dpj' 
basefile_name = direct_sim+'/voorbeeld_input' 
basefile_name_rel = 'voorbeeld_input'

# MATERIAL 1
# BASIC PARAMETERS (steeds ingeven als floats)
name1='DURIPANEL'
MEW1={'value':[41.0,55.0,82.0,123.0,163.0],'dist':'design','var':True}            
LAMBDA1={'value':[0.11,0.22,0.44],'dist':'design','var':True}    
KG1={'value':[0.05],'dist':'design','var':False}    

materials=['one']
properties=['NAME','MEW', 'LAMBDA', 'KG']
data=[[name1],[MEW1],[LAMBDA1],[KG1]]
Materials = DataFrame(data, columns=materials,index=properties)


   
###############################################################################
# NUMBER OF DESIGNS & UNCERTAINTIES FOR MATERIALS, GRIDS & CLIMATES (TO BOUNDARY LAYERS,...)
n_design=1
n_uncert=0
index_m=[]
for i in Materials:
    for j in Materials.index:
           if type(Materials[i][j])==dict:
               if Materials[i][j]['dist']=='design' and\
                  Materials[i][j]['var']==True:
                      n_design=n_design*len(Materials[i][j]['value'])
               if Materials[i][j]['dist']!='design' and\
                  Materials[i][j]['var']==True:
                      n_uncert=n_uncert+1               


###############################################################################

#  2  AANMAKEN VAN DE DESIGN (TO DO HIERNA AANMAKEN VAN DE SAMPLES)

basefile_obj = open(basefile_name + '.dpj', 'r')
basefile = basefile_obj.readlines()
del basefile_obj





# Looking for lines of  materialC:\Program Files (x86)\MiKTeX 2.9\miktex\bin to be changed and storing in mat_lines
mat_lines = Series([], dtype=int)
for i in Materials:   
        a=material_lines(Materials[i]['NAME'],basefile)
        mat_lines=mat_lines.append(a)

#MATERIALS IN DESIGNS
design_opt=[]
design_value=[]
for i in Materials:
    for j in Materials.index:
           if type(Materials[i][j])==dict:
               if Materials[i][j]['dist']=='design' and\
                  Materials[i][j]['var']==True:
                      design_opt.append(j+'_'+Materials[i]['NAME'])
                      design_value.append(Materials[i][j]['value'])





copyfile=list(basefile)        
copyfile[mat_lines['MEW_DURIPANEL']] = '      MEW                   = %g -\n' % 200
           
       
design_files=[]        
design_files.append(copyfile)



#wegschrijven van de design_files als er geen uncertainties worden meegenomen (parameter study) 
filename = basefile_name + '_%02d' % 1
filename_rel = basefile_name_rel + '_%02d' % 1
fileobj = open(filename + '.dpj', 'w')
fileobj.writelines(design_files[0])
del fileobj











###############################################################################
