import matplotlib.pyplot as plt
import numpy as np

# This loads the data that we are going to investigate
x = np.loadtxt("data.dat")

def dataFraction( data, ind ) :
  # Your code will go here
  
  
  
# Here is some code to test whether your function is working correctly
print( dataFraction(x, 49), "percent of the data points are less than the 49th element of the sorted array")
print( dataFraction(x, 99), "percent of the data points are less than the 99th element of the sorted array")
print( dataFraction(x, 149), "percent of the data points are less than the 149th element of the sorted array")
