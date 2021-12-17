import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.animation as animation




F = lambda t,s: np.dot(np.array([[0,t**2],[-t,0]]),s)

t_eval = np.arange(0, 5, 0.01) ##increase '5' to get more revz
sol = solve_ivp(F, [0, 5], [1, 1], t_eval=t_eval) ##increase '5' to get more revz



plt.figure(figsize = (12, 8))
plt.plot(sol.y.T[:, 0], sol.y.T[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()