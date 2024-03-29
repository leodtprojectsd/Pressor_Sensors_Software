"""
Scatter_fade.py has on xaxis = PIN and y = R, time shows in the title.
The plot is used to monitor each pin with a fade leaving a trace to track better movements.

"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import config
import functions_pressure as funp
from matplotlib.animation import FuncAnimation
import time


 #set ylim based on if fitting is true or False
ylim, y_title = (config.Y_lim, "R") if config.FITTING == False else ([0,1], "R - Norm")
print(f"Fitting data (MinMaxScaler): {config.FITTING}")

 #Start plot
fig, ax = plt.subplots()

ax.set_xlabel('PINS', size=12)
ax.set_ylabel(y_title, size=12)

ax.axis([0, max(config.PINS) + 1, ylim[0], ylim[1]])
ax.set_xticks(config.PINS)

x_vals = []
y_vals = []

iterations = 100

cmaps = [cm.get_cmap(x) for x in config.colors_fade] # get colors
cmaps = [cmaps[i] for i in config.PINS - 1] #only get colors for pins you need.

scatters = [ax.scatter(x_vals, y_vals, c=[], cmap=cmaps[i], vmin=0, vmax=1) for i in range(len(cmaps))]
intensities = [[] for i in range(len(cmaps))]  # initializing intensities array
start = time.time()


def get_new_vals():
    data = funp.read_lastnlines(config.paths_["DATA_FILENAME"], config.BUFFER_mean)
    if config.FITTING:
        scaler = funp.read_from_pickle(config.paths_["FIT_MINMAX_FILENAME"])
        data[:, 1:] = scaler.transform(data[:, 1:])
    time_ = data[:, 0][0]
    x = config.PINS
    y = data[:, 1:][0]
    y = [y[i] for i in config.PINS - 1]
    return x, y, time_


def animate(t):
    loop_time = time.time()
    global x_vals, y_vals, intensities
    # Get intermediate points
    new_xvals, new_yvals, time_ = get_new_vals()
    x_vals = np.hstack((x_vals, new_xvals))
    y_vals = np.hstack((y_vals, new_yvals))

    # Put new values in your plot
    for i in range(len(config.PINS)):
        scatters[i].set_offsets(np.c_[x_vals[x_vals == i + 1], y_vals[x_vals == i + 1]])
        intensities[i] = np.concatenate((np.array(intensities[i]) * 0.80, np.ones(len(new_xvals[new_xvals == i + 1]))))
        scatters[i].set_array(intensities[i])

        # Set title

    ax.set_title("Scatter fade \ntime {:0.3f} loop time:{:0.3f}".format(time.time() - time_, time.time() - loop_time))


def plot_():
    anim = FuncAnimation(fig, animate, interval=100)
    plt.show()
    plt.close()


if __name__ == '__main__':
    plot_()
