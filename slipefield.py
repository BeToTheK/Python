#Sketch a slope field for x'=x+t


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp
#dy(t)/dt=-ky(t)
def model(t,y,k):
	dydt= -k*y
	return dydt

#initial condition
y0 = 5

#time points
t=np.linspace(0,20)
k=0.1
y1=sp.odeint(model,y0,t,args=(k,))
plt.plot(t,y1)
k=0.1
y1=sp.odeint(model,y0,t,args=(k,))
plt.plot(t,y1)
plt.show()




