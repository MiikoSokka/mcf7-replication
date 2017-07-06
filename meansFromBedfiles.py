#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:33:30 2017

@author: Miiko
"""
import argparse
import csv
import sys

parser = argparse.ArgumentParser(description='''
                                 Description:
                                     This script transforms the ranges in bed file to means; i.e. gets the middle point of the each range.
                                     ''')

parser.add_argument('-i',
                    type = str,
                    help = '''Input file in standard bed format, with column1=name, column2=start and column3=end''',
                    required = True)

args = parser.parse_args()

bedfile = args.i

'''Get data from input file and organize in lists named cols[x], where x is column number starting from 0'''
MAXCOLS = 4
MAXLINES = 0
cols = [[] for _ in range(MAXCOLS)]
with open(bedfile) as input:
    for row in csv.reader(input, delimiter='\t'):
        MAXLINES += 1
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')

#change nested lists into single lists and change the type from str to int
colChr = cols[0]
colStart = list(map(int, cols[1]))
colEnd = list(map(int, cols[2]))
colStrand = cols[3]

#get the range means/peaks
#map method would be derived from: colPeak = list(map(operator.sub, colEnd, colStart)). import operator must be added if this is used.
colPeak = [int(round(float((i + j)/2))) for i, j in zip(colEnd, colStart)]

colStarts = list(map(str, colStart))
colEnds = list(map(str, colEnd))
colPeaks = list(map(str, colPeak))

for i in range(MAXLINES):
#    sys.stdout.write(colChr[i] + "\t" + colStart[i] + "\t" + colEnd[i] + "\t" + colPeak[i] + "\n")    
     sys.stdout.write(str(colChr[i]) + "\t" + str(colPeaks[i]) + "\n")
             #str(colChr[i]) + "\t" + str(colStarts[i]) + "\t" + str(colEnds[i]) + "\t" + str(colStrand[i]) + "\t" + str(colPeaks[i]) + "\n")    
    
    