# ENGR2050_11_jasayles.py
# Ethan Sayles
# April 27, 2017
import numpy as np

#Class to find the root of a function
class RootFinder:
    def __init__(self, function, a, b, value=0, iterations = 1000, tolerance = 1e-4):         #a function, left endpoint, right endpoint, value, number of tries, and tolerance
        self.func = function
        self.value = value
        self.tol = tolerance
        self.root = False
        self.a = a
        self.b = b
        self.its = iterations
    def close(self, A):                                                            #Check if a value is within the tolerance
        if np.abs(self.func(A)-self.value) <= self.tol:
            return True
        else:
            return False
            
    def root_finder(self):                                                    #Check if there is a zero with the given bounds
        steps = 1
        while steps < self.its:
            c = (self.b+self.a)/2
            if self.close(self.a):
                return (self.a)
            elif self.close(self.b):
                return (self.b)
            elif self.close(c):
                return (c)
            else:
                if self.func(c) * self.func(self.b) < 0:           #Check if the zero is between the midpoint and the right endpoint
                    self.a = c
                elif self.func(c) * self.func(self.a) < 0:         #Check if the zero is between the midpoint and the left endpoint
                    self.b = c
                else:
                    return ("Midpoint cannot be calculated using the given bounds.")
                
            steps += 1
        return ("Midpoint not found after %f steps. Please select smaller bounds." %(self.its))
        
    def bisect(self):                                                         #format the respose correctly
        zero = self.root_finder()
        if isinstance(zero, float):
            return ("Zero occurs at f(%4.5g)" %(zero))
        elif isinstance(zero, int):
            return ("Zero occurs at f(%4.5g)" %(zero))
        else:
            return zero                                                           #This is the case where there is an error.
           

#Conditional to check for test cases
if __name__ == '__main__':
    f = lambda x: (x**3 -5*x + 4) * np.sin(2*x)    
    thing = RootFinder(f, -4, 0, 1e-5)
    print( thing.bisect())
    
