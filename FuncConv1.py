import numpy as np
import matplotlib.pyplot as plt

def func(n,x):
	return (x**2+n*x)/n


ydata = []
xdata = []
def get_data(n):
	for a in np.arange(-5,5,.01):
	#print(func(1,a))
		ydata.append(func(n,a))
		xdata.append(a)
	return xdata,ydata
plt.title("Uniform Convergence of Function: (x^2+n*x)/n")
plt.axhline(0,color="black")
plt.axvline(0,color="black")

for i in range(0,25,3):
	get_data(i)
	plt.plot(xdata,ydata,label=i)
	plt.legend()
	xdata.clear()
	ydata.clear()


# fig, ax=plt.subplots()
plt.show()
