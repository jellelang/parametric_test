# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:51:21 2015

@author: Wout
"""

from __future__ import division
import sys,os

import pandas as pd
from pandas import Series, DataFrame

import subprocess
from subprocess import call

from utilityfunctions import *

direct_sim='C:/Users/Wout/OneDrive/LOCIE/Case/TRNSYS/'
sys.path.append(direct_sim) #voegt deze folder toe aan de toegankelijke paths

#define trnsys inputfile (dck-file)
dckfile=direct_sim+'INCAS_stochbehav.dck'

#read in inputfile into list with each line saved in each subsequent element
basefile_obj = open(dckfile, 'r')
basefile = basefile_obj.readlines()
del basefile_obj

#find and replace external file behavioural profile
oldlineprof='ASSIGN "C:\Users\Wout\Dropbox\LOCIE\Case\Inputfiles\profile1.txt" 31\n'
newlineprof='ASSIGN "C:\Users\Wout\Dropbox\LOCIE\Case\Inputfiles\profile2.txt" 31\n'
basefile=firepline(oldlineprof,newlineprof,basefile)

#write dckfile
basefile_obj=open(dckfile,'w')
basefile_obj.writelines(basefile)
del basefile_obj

#run TRNSYS
call('C:\Trnsys17\Exe\TRNExe.exe '+dckfile+' /h')

