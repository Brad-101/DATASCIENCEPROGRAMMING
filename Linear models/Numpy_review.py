#1D array 
import numpy as np

x = np.array([1,2,3,4,5])
print("The array is:",x)
#2D array
y = np.array([[1,2],[3,4]])
print(y)

#Generating random numbers in numpy
#random float btw 0 and 1 , this is possible through the rand() function in numpy
randon_float= np.random.rand()
print("These are the randomfloat:",randon_float)

a= np.random.rand(3,3)
print("These are the random float array:",a)

#Generating random integers in numpy
#random integer between 0 and 10, this is possible through the randint() function in numpy
b = np.random.randint(50,10000,20)
print("This is the random integer:",b)  

#normal distribution in numpy
#normal distribution with mean 0 and standard deviation 1, this is possible through the normal() function in numpy
c= np.random.normal(0,1,10)
print("This is the normal distribution:",c) 

#seed() function in numpy
#seed the random number generator to get the same random numbers every time, this is possible through the seed() function in numpy
np.random.seed(45)
d = np.random.randint(3,30,5)
print("This is the random integer array with seed:",d)

#zero() function in numpy
#creating an array of zeros, this is possible through the zeros() function in numpy
e = np.zeros((3))
print("This is the array of zeros:",e)

#ones() function in numpy
#creating an array of ones, this is possible through the ones() function in numpy               
f = np.ones((2,3))
print("This is the array of ones:",f)   

#linspace() function in numpy
#creating an array of evenly spaced numbers over a specified interval, this is possible through the linspace() function in numpy
g = np.linspace(0,10,5) 
print("This is the array of evenly spaced numbers:",g)

#reshape() function in numpy
#reshaping an array, this is possible through the reshape() function in numpy
h = np.arange(12)
print("This is the original array:",h)
i = h.reshape(3,4)
print("This is the reshaped array:",i)