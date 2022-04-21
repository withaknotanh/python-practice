# Find e to the Nth Digit 
# Enter a number and have the program generate e up to that many decimal places. 
# Keep a limit to how far the program will go.

import numpy as np 

def yumE(n):
    if n < 20:
        return(round(np.e, (n-1))) 
    else: 
        print("integer out of bounds")


print(yumE(4))
