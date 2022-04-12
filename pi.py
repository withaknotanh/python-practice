# Find PI to the Nth Digit 
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

#rebecka version 
import numpy 

space = int(input("enter an integer less than 20"))                 #prompts user to enter integer 

if space < 20:                                                      #if in bounds, round pi to the inputted integer amount
    print(round(numpy.pi, space))

else:
    print("integer out of bounds")  
