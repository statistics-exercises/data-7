import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_isSorted(self) : 
       myx = np.loadtxt("data.dat")
       for i in range(len(myx)) :
          self.assertTrue( np.abs( myx[i] - x[i])<1e-8, "You do not need to sort the variable called x" )
          
    def test_function(self) : 
       for i in range(len(x) ) :
          ppp = i / (len(x)-1) 
          self.assertTrue( np.abs( 100*ppp - dataFraction(x,i) )<1e-9, "Your function for evaluating the percentage is incorrect" )
