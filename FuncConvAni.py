import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
x1=[]
y1=[]
def f1(x):
	return x

for i in range(-4,5):
	ans = f1(i)
	x1.append(ans)
	y1.append(ans)


def func_one(x,n):
	return (x**2+n*x)/n

fig, ax = plt.subplots()
x = np.arange(-4,4,.001)
line, = ax.plot(x, func_one(x,20)) #ani stops at f(20)
plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.plot(x1,y1)
plt.grid()


def animate(i):
    line.set_ydata(func_one(x,i/5))
    	  # update the data.
    return line,

plt.title("Uniform Convergence of a Function: (x^2+n*x)/n")


ani = animation.FuncAnimation(
    fig, animate, interval=100, blit=True, save_count=500)
plt.show()

#ani.save("FConverges.mp4")

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#


# f = r"c://Users/bk/Pictures/anime/convg.gif" 
# writergif = animation.PillowWriter(fps=30) 
# ani.save(f, writer=writergif)