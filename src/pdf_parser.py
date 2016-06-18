# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:34:44 2016

@author: Alex Kerr
"""

import sys

import slate

#paper = sys.argv[1]
paper = "math.pdf"

def main():
    
    with open(paper) as f:
        papertext = slate.PDF(f)
        
    print(papertext)
    
main()