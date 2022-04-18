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


for x in incrimentFun(1.5, 10.5, 2):
  print(x)
