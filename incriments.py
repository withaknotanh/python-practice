#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:03:59 2022

@author: rebeckamoreno
"""
#Create a for loop to increment by .1 at each iteration 
#Outputs to console

#rebecka version
import numpy as np

for x in np.arange(0, 1, 0.1):          #range is from 0 to 1 in 0.1 incriments
    print(x)


#more robust rebecka version?
lower = int(input("enter min"))
upper = int(input("enter max"))
incriment = int(input("enter incriment"))  

for x in np.arange(lower, upper, incriment):          
    print(x)
