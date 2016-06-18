# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:34:44 2016

@author: Alex Kerr
"""

from sys import argv
import slate

script,paper = argv


def main():
    
    with open(paper) as f:
        papertext = slate.PDF(f)
        
    print(papertext)
    
main()
