import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_gen():
    t = data_gen.t
    cnt = 0
    while cnt < 1000:
        cnt+=1
        t += 0.05
        y1 = np.sin(2*np.pi*t) * np.exp(-t/10.)
        y2 = np.cos(2*np.pi*t) * np.exp(-t/10.)
        y3 = np.cos(3*np.pi*t) * np.exp(-t/10.)
        # adapted the data generator to yield both sin and cos
        yield t, y1, y2, y3




data_gen.t = 0

# create a figure with two subplots
fig, (ax1, ax2, ax3) = plt.subplots(3,1)

# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line3, = ax3.plot([], [], lw=2, color='black')

line = [line1, line2, line3]

# the same axes initalizations as before (just now we do it for both of them)
for ax in [ax1, ax2, ax3]:
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 5)
    ax.grid()

# initialize the data arrays
xdata, y1data, y2data , y3data = [], [], [], []
def run(data):
    # update the data
    t, y1, y2, y3 = data
    xdata.append(t)
    y1data.append(y1)
    y2data.append(y2)
    y3data.append(y3)

    # axis limits checking. Same as before, just for both axes
    for ax in [ax1, ax2, ax3]:
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(xdata, y1data)
    line[1].set_data(xdata, y2data)
    line[2].set_data(xdata, y3data)

    return line

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
    repeat=False)
plt.show()