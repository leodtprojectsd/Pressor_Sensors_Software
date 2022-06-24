'''
Test pressure matrix plots scatte plot dots over the sensor pixels,
with colour changing based on sensor condition.
'''

import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import os

# min and max values that the sensors will produce
SENSOR_MIN = 0
SENSOR_MAX = 1

def make_plot(background, coordinates, pressure_data):
    fig, ax = plt.subplots(1, 1)
    ax.imshow(background)

    coordinates = np.asarray(coordinates).reshape(-1, 2).T
    sc = ax.scatter(
        *coordinates,
        s=10.0**2,
        c=pressure_data.reshape(-1),
        cmap="inferno",
        vmin=SENSOR_MIN,
        vmax=SENSOR_MAX,
    )
    fig.colorbar(sc, label="pressure (some units)")
    return fig, sc

def update_plot(fig, sc, pressure_data):
    """Update the plot with new data and redraw the figure."""
    sc.set_array(pressure_data.reshape(-1))
    fig.canvas.draw()
    fig.canvas.flush_events()

def get_data():
    return np.random.random((2, 8))

if __name__ == "__main__":
    image_filepath = os.path.join(os.getcwd(), "background_images", "example_image.png")
    background_img = plt.imread(image_filepath)
    # pixel coordinates of each sensor in the background image
    coords = [[[462, 106],
               [547, 113],
               [430, 156],
               [601, 237],
               [543, 222],
               [497, 221],
               [430, 216],
               [444, 266]],
              [[489, 439],
               [609, 463],
               [613, 564],
               [500, 574],
               [568, 641],
               [524, 643],
               [577, 688],
               [527, 683]]]

    fig, sc = make_plot(background_img, coords, get_data())
    # exit the script when the figure is closed
    fig.canvas.mpl_connect("close_event", lambda event: sys.exit())
    plt.show(block=False)

    # draw some data in loop
    while True:
        frame_start = time.perf_counter()
        pressure_values = get_data()
        # update the figure
        update_plot(fig, sc, pressure_values)
        # wait for 0.1s (including the time it took to update the plot)
        frame_time = time.perf_counter() - frame_start
        if frame_time < 0.1:
            plt.pause(0.1 - frame_time)