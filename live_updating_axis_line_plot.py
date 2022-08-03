import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import time
import config
import functions_pressure as funp

def data_gen():
    t = data_gen.t

    d = np.random.randint(0, 10, (2, 32)).astype(float)
    now_time = time.time() - start_time # get current time from start to append
    d = (np.insert(d, 0, [now_time,now_time+ 1/62.5], axis=1)).tolist()
    d = funp.read_lastnlines(config.paths_["DATA_FILENAME"], config.BUFFER_mean)
    yield t, d

data_gen.t = 0

fig, axes = plt.subplots(2,2)

axr = axes.ravel()
COLOR = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
# lines = {f"line{i}": axr[i//8].plot([1,2], [3,4], lw=2) for i in range(0,32)} #
# line_list = [item for sublist in lines.values() for item in sublist]
lines = [axr[i//8].plot([], [], lw=2, color=COLOR[i], label=i+1)[0] for i in range(0,32)]


[(ax.set_ylim(config.SENSOR_MIN, config.SENSOR_MAX), ax.set_xlim(0, 40), ax.grid(), ax.title.set_text(f"PINS {(idx*8+1)} to {(idx*8+9)}"),
  ax.legend(loc='lower right', bbox_to_anchor=(1.1, 0.3))) for idx, ax in enumerate(axr)]

 #iniitiliaze the data arrays
start_time = time.time()
store_data = np.zeros((1, 33))

def run(data):
    global store_data, lines
    # update the data
    t, d = data
    time_ = store_data[-1:, 0][0] -start_time
    store_data = np.append(store_data, d, axis=0)
    # axis limits checking. Same as before, just for both axes
    for ax in axr:
        xmin, xmax = ax.get_xlim()
        if time_ >= xmax:


            # plt.cla()
            # lines = [axr[i // 8].plot([], [], lw=2, color=COLOR[i])[0] for i in range(0, 32)]

            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()


    # update the data of both line objects

    for idx, line in enumerate(lines):
        # print (store_data[:, 0][0], store_data[:,int(line[-1])])
        lines[idx].set_data(store_data[:, 0]-start_time, store_data[:,idx])
        # lines[line][0].set_data(store_data[:, 0][0], store_data[:,int(line[-1])]) #BUG, line is in a list so need to use [0]

    return lines #[item for sublist in lines.values() for item in sublist]

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
    repeat=True)

plt.show()

