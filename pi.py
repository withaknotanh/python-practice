# Find PI to the Nth Digit 
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

import numpy as np 

def yummyPi(n):
    if n < 20:
        print(round(np.pi, (n-1))) 
    else: 
        print("integer out of bounds")


for x in yummyPi(4):
    print(x)
