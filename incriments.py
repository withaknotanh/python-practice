#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:03:59 2022

@author: rebeckamoreno
"""
#Create a for loop to increment by .1 at each iteration 
#Outputs to console

def incrimentFun(start, end, incriment):
    while start < end:
        yield start
        start = start + incriment

list = incrimentFun(1, 2, 0.1)

for x in list:
  print(x)
