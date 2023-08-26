# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

# Define figure, axes and sliders
fig = plt.figure(figsize=(10, 10))
ax = plt.axes([0.1, 0.45, 0.8, 0.45])
sliders_handle = [] 

time_ax = plt.axes([0.18, 0.3, 0.7, 0.03])
sliders_handle.append(widgets.Slider(time_ax, 'Max Time', 0, 1000, valinit = 5.0))
omega_ax = plt.axes([0.18, 0.25, 0.7, 0.03])
sliders_handle.append(widgets.Slider(omega_ax, 'Omega', 0.1, 1, valinit = 1))
ohm_ax = plt.axes([0.18, 0.2, 0.7, 0.03])
sliders_handle.append(widgets.Slider(ohm_ax, 'Ohm', 0.01, 1, valinit = 0.01))

#Define the parametric functions
def x(t, omega, ohm):
    return np.cos(ohm * t) * np.cos((omega * np.sqrt((1 + (ohm ** 2)) / (omega ** 2))) * t)
def y(t, omega, ohm):
    return -1 * np.sin(ohm * t) * np.cos((omega * np.sqrt((1 + (ohm ** 2)) / (omega ** 2))) * t)

# Define a slider_callback for our sliders
def slider_callback(event):
    ax.clear()
    time =  sliders_handle[0].val
    omega = sliders_handle[1].val
    ohm = sliders_handle[2].val
    plot(time, omega, ohm)

# Define a plotting function
def plot(time, omega, ohm):
    t = np.linspace(0, time, 5000)
    ax.set_xlabel("x in metres")
    ax.set_ylabel("y in metres")
    ax.set_title("Foucault Pendulum")
    #ax.set_ylim(-0.5,0.5)
    ax.plot(x(t,omega,ohm),y(t,omega,ohm))
    plt.show()
    
# Add callback to sliders now we have written the slider_callback
for slider_handle in sliders_handle:
    slider_handle.on_changed(slider_callback)
    
plot(5, 1, 0.01)