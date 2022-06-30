"""
Plot pixel lines (scatter for now) over large period of time.
"""


 # modifying from https://stackoverflow.com/questions/23049762/matplotlib-multiple-animate-multiple-lines
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import random
import functions_pressure as funp
import config
import time
import numpy as np

ylim = (0, 5e7)
xlim = (0, 200)
lw= 2

fig = plt.figure(figsize=(10, 8))
ax1 = plt.axes(xlim=xlim, ylim=ylim) # todo make these valules config
line, = ax1.plot([], [], lw=lw, marker=".", ms=8) #todo config
plt.xlabel("time[s]")
plt.ylabel("RΩ")
#todo set lengend
lines = []
store_data = np.zeros((1, 33))
for i in range(1, store_data.shape[1]):
    lobj = ax1.plot([], [], lw=lw, marker=".",  ms=8, color=config.COLOURS[i - 1])[0]
    lines.append(lobj)

def init():
    for line in lines:
        line.set_data([], [])
    return lines


store_data = np.zeros((1, 33))

# fake data
frame_num = 100
def animate(i):
    global store_data

    data = funp.read_lastnlines(config.DATA_FILENAME, 62) #todo config
    # data[:,1:] = np.reciprocal(data[:,1:]) # this is for conductance - (change ylim range )
    store_data = np.append(store_data, data, axis=0)
    for lnum,line in enumerate(lines):
        line.set_data(store_data[:,0], store_data[:,lnum]) # set data for each line separately.
    return lines

def plot_():
    print ("waiting a bit for data to start a writing..(sleeping 5 seconds)")
    # time.sleep(5)
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=frame_num, interval=10, blit=True)
    plt.show()
    plt.close()

if __name__ == '__main__':
    plot_()