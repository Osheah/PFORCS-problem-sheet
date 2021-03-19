#  program that displays a plot of the functions f(x) = x, g(x) = x**2, h(x) = x**3 and make the plot look fancy
# helen oshea
# 20210311

# import the modules 
import numpy as np # needed for creating the x axis
import matplotlib.pyplot as plt # needed for ploting



x  = np.arange(0,4, .1) # create the x axis
fx= x # the line y = x
gx = x**2 # the curve y = x squared
hx = x**3 # the curve y = x cubed


plt.title('plot of x, x**2, x**3') # the title of the plot
plt.xlabel('x') # the x axis label
plt.ylabel('y') # the y axis label
plt.plot(x, fx, label='x') # the line
plt.plot(x, gx, label='x**2') # the quadratic curve
plt.plot(x, hx, label='x**3') # the cubic curve
plt.legend() # show the labels
plt.savefig('plottask.jpg')
plt.show() # show the plot
