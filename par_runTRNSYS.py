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

direct_sim='C:/Users/Wout/OneDrive/LOCIE/Case/TRNSYS/'
sys.path.append(direct_sim) #voegt deze folder toe aan de toegankelijke paths

dckfile=direct_sim+'INCAS_stochbehav.dck'

call('C:\Trnsys17\Exe\TRNExe.exe '+dckfile+' /h')

