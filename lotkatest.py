import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp
#Suppose there are two species of animals, 
#a baboon (prey) and a cheetah (predator). 
#If the initial conditions are 10 baboons and 10 cheetahs, 
#one can plot the progression of the two species over time; 
#given the parameters that the growth and death rates of 
#baboon are 1.1 and 0.4 while that of cheetahs 
#are 0.4 and 0.1 respectively. 
#The choice of time interval is arbitrary.
# *Lotka-Volterra Wiki 
def lotka(t,z,a,b,c,d):
	x,y=z
	return[a*x-b*x*y,-c*y+x*d*y]

sol = sp.solve_ivp(lotka, [0, 100], [10, 10], args=(1.1, 0.4, 0.4, 0.1),
                dense_output=True)
t = np.linspace(0,101,300)
z= sol.sol(t)
plt.plot(t,z.T)
plt.xlabel
plt.legend(['Prey', 'Predator'])
plt.xlabel('Time in Years')
plt.ylabel('Population x10^3')
plt.show()