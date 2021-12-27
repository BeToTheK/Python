import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def f(t):
    x = (2+np.cos(1.5*t))*np.cos(t)
    y = (2+np.cos(1.5*t))*np.sin(t)
    z = np.sin(1.5*t)
    lineData = np.array((x,y))
    return lineData

def init():
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(f(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(0, 25, 0.1),
                    init_func=init, blit=True)
plt.show()