"""
This plot does 4 subplots (one for each DAC) with R lines divided by pixels.

- x_lim update: X axis updates giving a + config.separate_x_lim_increment each time.
- y_lim: You can set 4 different y scales with config.separate_y_lim
- start time: Plot takes away its run time from data acquisition --> always starts with t=0

PLOT DOES NOT LET YOU SELECT PINS TO VIEW, you'd have to modify the code a bit
I did not make this plot to run in multiprocess, you'd have to rework the global variables (start time etc.)
"""


import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import time
import config
import functions_pressure as funp

def data_gen():
    """
    data_gen yelds time and d(data), It doesn't support Fitting - you can easily modify if you need it.
    :yeld: t, d
    """
    t = data_gen.t
    d = funp.read_lastnlines(config.paths_["DATA_FILENAME"], config.BUFFER_mean)
    yield t, d

data_gen.t = 0

# plt.style.use("fivethirtyeight")
fig, axes = plt.subplots(2,2)

 #all ax in one list
axr = axes.ravel()
 #start updating each ax
lines = [axr[i//8].plot([], [], lw=2, color=config.separate_COLOR[i], label=i+1)[0] for i in range(0,32)]
 #configure for each ax
[(ax.set_ylim(config.separate_y_lim[idx][0], config.separate_y_lim[idx][1]),
  ax.set_xlim(config.separate_x_lim[0], config.separate_x_lim[1]),
  ax.grid(),
  ax.title.set_text(f"PINS {(idx*8+1)} to {(idx*8+9)}"),
  ax.legend(loc='lower right', bbox_to_anchor=(1.1, 0.1))) for idx, ax in enumerate(axr)]

def run(data):
    global store_data, lines, start_time
    # update the data
    t, d = data
    time_ = store_data[-1:, 0][0] - start_time
    store_data = np.append(store_data, d, axis=0)
    # axis limits checking. Same as before, just for both axes
    for ax in axr:
        xmin, xmax = ax.get_xlim()
        if time_ >= xmax:

            ax.set_xlim(xmin, config.separate_x_lim_increment+xmax)
            ax.figure.canvas.draw()
    # update the data of both line objects

    for idx, line in enumerate(lines):
        # print(idx, line.get_label())
        lines[idx].set_data(store_data[:, 0]-start_time, store_data[:,idx+1])
    return lines #[item for sublist in lines.values() for item in sublist]

#main
if __name__ == '__main__':
    start_time = time.time()
    store_data = np.zeros((1, 33))
    ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
        repeat=True)

    plt.show()