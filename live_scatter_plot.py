"""
Live import from CSV and produce 2 line scatter plot (from average over 20 points
"""
import config
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import functions_pressure as funp
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")

def animate(i):
	data = funp.read_lastnlines(DATA_FILENAME, 20)
	x = data[:, 0]
	plt.cla()
	 #configure after cla
	ax.set_ylim(config.Y_lim)
	ax.set_title("Live R vs Time for each pixel")
	ax.set_xlabel("time[s]")
	ax.set_ylabel("RΩ")

	for pin in config.PINS:
		plt.scatter(x, data[:, pin], c=config.colours[pin - 1], label=f"channel_{pin}")
	plt.legend(list(config.PINS), loc=(1.04, 0))
	plt.tight_layout()


# main
def plot_():
	anim = FuncAnimation(plt.gcf(), animate, interval=100)
	plt.show()
	plt.close()


plt.style.use("fivethirtyeight")
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.set_title("Live R vs Time for each pixel")
ax.set_xlabel("time[s]")
ax.set_ylabel("RΩ")
plt.tight_layout()

if __name__ == '__main__':
	PINS = np.arange(1, 5)
	colours = [f"C{i}" for i in range(1, 33)]
	plot_()
