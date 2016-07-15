# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:34:44 2016

@author: Alex Kerr
"""

from sys import argv
import slate

script,paper = argv


def main():
    output_file = open('text_from_pdf.txt','w')
    with open(paper) as f:
        papertext = slate.PDF(f)
        
    for i in range(0,len(papertext)):
        output_file.write(papertext[i])

main()
