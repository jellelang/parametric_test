# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:42:47 2015

@author: Wout
"""

from __future__ import division

#------------------------------------------------------------------------------
# Function firepline to find and replace a line of text in a file
# Input: text on existing line, text for new line and basefile as list
# Output: basefile as list with replaced line
def firepline(oldline,newline,basefile):
    line_changes=-1
    ok=True
    for i in basefile:
        line_changes=line_changes+1
        if i == oldline:
            ok=False    
            basefile[line_changes]=newline
            break
    if ok:
        print('ERROR!!!  %s not found' % oldline)
        
    return basefile