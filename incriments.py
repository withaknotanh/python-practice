#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:03:59 2022

@author: rebeckamoreno
"""
#Create a for loop to increment at each iteration 
#Console outputs 
#Must work for negative and float numbers
#Can incremenet upwards and backwards

def incrementFun(start, end, increment):
    while start < end:                      # allows to increment upwards
        yield start
        start = start + increment

    while start > end:                      # allows to increment backwards 
        yield start
        start = start - increment 

for x in incrementFun(10.5, 1.5, 0.1):
  print(x)
