"""
Live import from CSV and produce 2 line scatter plot (from average over 20 points
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import functions_pressure as funp
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")


def animate(i):
	#get data
	data = funp.read_lastnlines(DATA_FILENAME, 20)

	x = data[:, 0]
	y = data[:, 1]
	y2 = data[:, 2]
	plt.cla()
	ax.set_ylim([0, 255])
	ax.scatter(x, y, label="channel_1")
	ax.scatter(x, y2, label="channel_2")

	plt.legend(loc="upper left")
	plt.tight_layout()

#main

def plot_():
    anim = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.show()
    plt.close()


plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.set_title("Plot of random numbers from `gen.py`")
ax.set_xlabel("time / s")
ax.set_ylabel("random number / #")
plt.tight_layout()

if __name__ == '__main__':
    plot_()
