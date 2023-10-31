# Imports 
import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 

# Define constants
OMEGA = 1
OHM = 0.628

# Define plot
fig = plt.figure() 
ax = plt.axes(xlim = (-1.1, 1.1), ylim = (-1.1, 1.1)) 
ax.set_title('Foucault Pendulum Animation')
ax.set_xlabel('Distance x in metres')
ax.set_ylabel('Distance y in metres')
line, = ax.plot([], [], lw = 2) 
x_data, y_data = [], [] 

# Initial function for the animation
def init(): 
    line.set_data([], []) 
    return line, 

# Define parametric functions
def x(t):
    return np.cos(OHM * t) * np.cos((OMEGA * np.sqrt((1 + (OHM ** 2))/(OMEGA ** 2))) * t)
def y(t):
    return -1 * np.sin(OHM * t) * np.cos((OMEGA * np.sqrt((1+(OHM**2))/(OMEGA ** 2))) * t)

# Define animation function
def animate(i): 
    # t is a parameter which varies with the frame number 
    t = 0.025 * i 
    # Appending values to the previously empty x and y data holders 
    x_data.append(x(t)) 
    y_data.append(y(t))
    line.set_data(x_data, y_data) 
    return line,

# Call the animation function     
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                               frames = 1000, interval = 14, blit = True) 
