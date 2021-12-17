import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
x1=[]
y1=[]
def func_one(x):
	if np.all(x)==0:
		return 0
	else:
		return x*np.sin(1/x)
#we are looking as x ranges from -0.25 to 0.25
#taking +.001 steps **
fig, ax = plt.subplots() #makes the "subplot" or what we build on
x = np.arange(-.25,.25,.001) #**
line, = ax.plot(x, func_one(x)) #plots func_one over the range x
plt.axhline(0,color="black") #adds horz axis
plt.axvline(0,color="black") #adds vert axis
plt.grid() #simple grid
plt.title("The function xsin(1/x) near zero.")



def animate(i):
    line.set_ydata(func_one(x/[(i+.1)]*20))
    #print(i)
    	  # updates the data instatly as animate loops through
    	  # the function calling x each time.
    	  # it seems animate indexes from zero and that would cause
    	  # '1/0' in line 22. Since we are looking at zero i have to
    	  # first add a small amount to the animate index 'i' and then
    	  # multiply that qty up for a decent runtime. 
    	  # there are variations here for speed control.
    return line,



ani = animation.FuncAnimation(
    fig, animate, interval=100, save_count=500)
#built in function(most basic build), 
#call the fig or subplot we initialized to draw on
#call animate to get the x and y data continuosly
#interval is delay between frames 100 seems to work
#,BLIT=TRUE, also works for optimized drawing
#save_count for saving how long the anime is 

#****//////FROM MATPLOTLIB//////*****
#'Fallback for the number of values from frames to cache. 
#This is only used if the number of frames cannot be 
#inferred from frames, 
#i.e. when it's an iterator without length or a generator.'


#***///ONLY USED TO SAVE/////*****
# f = r"c://Users/bk/Pictures/anime/convergencex.gif" 
# writergif = animation.PillowWriter(fps=30) 
# ani.save(f, writer=writergif)

plt.show()