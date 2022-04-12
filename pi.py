# Find PI to the Nth Digit 
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

#rebecka version 
import math 
import numpy 

space = int(input("enter an integer less than 20"))

if space < 20:
    print(round(numpy.pi, space))

else:
    print("integer out of bounds")
