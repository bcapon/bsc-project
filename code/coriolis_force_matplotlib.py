# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

# Define variables
g = 9.8
v = 10
omega = 0.626
time = 3
launch_height = 1

# Setup figure, axes and sliders
fig = plt.figure(figsize=(10, 10))
ax = plt.axes([0.1, 0.45, 0.8, 0.45])
sliders_handle = []

time_ax = plt.axes([0.18, 0.3, 0.7, 0.03])
sliders_handle.append(widgets.Slider(time_ax, 'Max Time', 0, 10, valinit = 3.0))

omega_ax = plt.axes([0.18, 0.25, 0.7, 0.03])
sliders_handle.append(widgets.Slider(omega_ax, 'Omega', 0, 5, valinit = omega))

v_ax = plt.axes([0.18, 0.2, 0.7, 0.03])
sliders_handle.append(widgets.Slider(v_ax, 'Vertical Velocity', 0, 20, valinit = 10))

y_max_ax = plt.axes([0.18, 0.15, 0.7, 0.03])
sliders_handle.append(widgets.Slider(y_max_ax, 'Maximum y', 1, 20, valinit = 5))

x_min_ax = plt.axes([0.18, 0.1, 0.7, 0.03])
sliders_handle.append(widgets.Slider(x_min_ax, 'Minimum x', -20, 0, valinit = -5))

x_max_ax = plt.axes([0.18, 0.05, 0.7, 0.03])
sliders_handle.append(widgets.Slider(x_max_ax, 'Maximum x', 0, 20, valinit = 5))

launch_height_ax = plt.axes([0.18, 0.35, 0.7, 0.03])
sliders_handle.append(widgets.Slider(launch_height_ax, 'Launch Height', 0, 2, valinit = 1))


# Define the parametric functions 
def x(t, omega, v):
    return (v / (2 * omega)) + ((g * np.sin(2 * omega * t)) / (4 * (omega ** 2))) - \
           ((v * np.cos(2 * omega * t)) / (2 * omega)) - ((g * t) / (2 * omega))
def y(t, omega, v, launch_height):
    return launch_height - (g / (4 * (omega ** 2))) + ((v * np.sin(2 * omega * t)) / (2 * omega)) + \
           ((g * np.cos(2 * omega * t))/(4 * (omega ** 2)))

# Define a slider_callback for our sliders
def slider_callback(event):
    ax.clear()
    time =  sliders_handle[0].val
    omega = sliders_handle[1].val
    v = sliders_handle[2].val
    y_max = sliders_handle[3].val
    x_min = sliders_handle[4].val
    x_max = sliders_handle[5].val
    launch_height = sliders_handle[6].val
    plot(time, omega, v, launch_height, y_max, x_min, x_max)

# Define a plotting function
def plot(time, omega, v, launch_height, y_max, x_min, x_max):
    t = np.linspace(0, time, 500)
    ax.set_xlabel("Distance x in metres")
    ax.set_ylabel("Distance y in metres")
    ax.set_title("Effect of Coriolis Force on Route")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0, y_max)
    ax.plot(x(t, omega, v), y(t, omega, v, launch_height))
    plt.show()

# Add callback to sliders now we have written the slider_callback
for slider_handle in sliders_handle:
    slider_handle.on_changed(slider_callback)
    
plot(time, omega, v, launch_height, 5, -5, 5)
