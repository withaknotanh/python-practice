# Find PI to the Nth Digit 
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

#rebecka version where n is decimal places
import numpy as np

n = int(input("enter an integer less than 20"))                 #prompts user to enter integer 

if n < 20:                                                      #if in bounds, round pi to the inputted integer amount after decimal
    print(np.round(np.pi, n))
else:
    print("integer out of bounds")  
    

#rebecka version where n is total places
import numpy as np

n = int(input("enter an integer less than 20"))                 #prompts user to enter integer 

if n < 20:                                                      #if in bounds, round pi to the inputted integer amount
    print(round(np.pi,(n-1)))
else:
    print("integer out of bounds")  
