import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#I solved this random diffeq. on Line 8 by hand then used the analytic answer
#to get a vizualization as this system changes its parameters. 
#DIFFEQ:  dy(t)/dt=-ky(t)
def y(t,k):
    return np.exp(-k*t)
# l=[]
# l1=[]
# l2=[]
# for i in np.linspace(0,20):
#     l2.append(y(i,0.2))
#     l1.append(y(i,1))
#     l.append(y(i,0.1))

# plt.plot(l)
# plt.plot(l1)
# plt.plot(l2)
# plt.show()


plt.style.use('seaborn-poster')

# F = lambda t, s: np.cos(t)

# t_eval = np.arange(0, np.pi, 0.1)
# sol = solve_ivp(F, [0, np.pi], [0], t_eval=t_eval)


F = lambda t,s: np.dot(np.array([[0,t**2],[-t,0]]),s)

t_eval = np.arange(0, 5, 0.01)
sol = solve_ivp(F, [0, 5], [1, 1], t_eval=t_eval)

plt.figure(figsize = (12, 8))
plt.plot(sol.y.T[:, 0], sol.y.T[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()