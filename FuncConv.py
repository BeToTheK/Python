import numpy as np
import matplotlib.pyplot as plt

def func(n,x):
	return (x**2+n*x)/n

def func1(n,x):
	return x*np.sin(1/x)
def fofo(x):
	return x




ydata = []
xdata = []
def get_data(n):
	for a in np.arange(-2,2,.01):
	#print(func(1,a))
		ydata.append(func(n,a))
		xdata.append(a)
	return xdata,ydata
plt.title("Uniform Convergence of Function: (x^2+n*x)/n")
plt.axhline(0,color="black")
plt.axvline(0,color="black")


for i in range(1,25,5):
	get_data(i)
	plt.axhline(0,color="black")
	plt.axvline(0,color="black")
	plt.plot(xdata,ydata,label=i)
	#plt.text(xdata[-1], ydata[-1], f'f({i})') this works but looks messy
	plt.legend()
	xdata.clear()
	ydata.clear()
# ntwrdi =  x 
plt.grid()
plt.show()
