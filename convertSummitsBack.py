#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:15:06 2017

@author: Miiko
"""

import argparse
import csv
import sys

parser = argparse.ArgumentParser(description='''
                                 Description:
                                     This script transforms the extended peak ranges back to summits.
                                     Input file is the 'paired' bed file that is generated with meansFromBedfiles.py.                                     ''')

parser.add_argument('-i',
                    type = str,
                    help = '''Input file in paired bed format: columns 1-5 are from intersect file A
                    (chr;start;end;name;value). Columns 6-9 are from intersect file B (chr;start;end;strand).
                    File A contains the peaks and file B contains G4 centers.''',
                    required = True)

args = parser.parse_args()

bedfile = args.i

'''Get data from input file and organize in lists named cols[x], where x is column number starting from 0'''
MAXCOLS = 9
MAXLINES = 0
cols = [[] for _ in range(MAXCOLS)]
with open(bedfile) as input:
    for row in csv.reader(input, delimiter='\t'):
        MAXLINES += 1
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')

#change nested lists into single lists and change the type from str to int when necessary
col1 = cols[0]
col2 = list(map(int, cols[1]))
col3 = list(map(int, cols[2]))
col4 = cols[3]
col5 = cols[4]
col6 = cols[5]
col7 = list(map(int, cols[6]))
col8 = list(map(int, cols[7]))
col9 = cols[8]

#add 1000bp to col2 and subtract 1000bp from col3
col2n = [i + 1000 for i in col2]
col3n = [i - 1000 for i in col3]

#change to str
col2new = list(map(str, col2n))
col3new = list(map(str, col3n))

for i in range(MAXLINES):
#    sys.stdout.write(colChr[i] + "\t" + colStart[i] + "\t" + colEnd[i] + "\t" + colPeak[i] + "\n")    
     sys.stdout.write(str(col1[i]) + "\t" + str(col2new[i]) + "\t" + str(col3new[i]) + "\t" + str(col4[i]) + "\t" + str(col5[i]) + "\t" + str(col6[i]) + "\t" + str(col7[i]) + "\t" + str(col8[i]) + "\t" + str(col9[i]) + "\t" + "\n")    
    