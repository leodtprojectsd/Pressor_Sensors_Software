#!/usr/bin/env python3
import functions_pressure as funp
import os
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation


def animate(i, xs, ys, limit=20, verbose=False):
    # grab the data
    try:
        data = funp.get_data(DATA_FILENAME, BUFFER_LEN)
        if verbose:
            print(data)
        x, y = map(float, data.split())
        if x > xs[-1]:
            # Add x and y to lists
            xs.append(x)
            ys.append(y)
            # Limit x and y lists to 10 items
            xs = xs[-limit:]
            ys = ys[-limit:]
        else:
            print(f"W: {time.time()} :: STALE!")
    except ValueError:
        print(f"W: {time.time()} :: EXCEPTION!")
    else:
        # Draw x and y lists
        ax.clear()
        ax.set_ylim([0, 1])
        ax.plot(xs, ys)

# show interactively
def plot_():
    anim = mpl.animation.FuncAnimation(fig, animate, fargs=([time.time()], [None]), interval=1)
    plt.show()
    plt.close()


BUFFER_LEN = 64
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.txt")
PLOT_LIMIT = 20
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.set_title("Plot of random numbers from `gen.py`")
ax.set_xlabel("time / s")
ax.set_ylabel("random number / #")
ax.set_ylim([0, 1])

if __name__ == '__main__':
    plot_()