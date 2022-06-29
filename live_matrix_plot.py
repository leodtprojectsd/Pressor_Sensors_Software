import config
import functions_pressure as funp
import sys
import time
import matplotlib.pyplot as plt
import numpy as np



def make_plot(background, coordinates, pressure_data):
    fig, ax = plt.subplots(1, 1)
    ax.imshow(background)

    coordinates = np.asarray(coordinates).reshape(-1, 2).T
    sc = ax.scatter(
        *coordinates,
        s=10.0**2,
        c=pressure_data.reshape(-1),
        cmap="inferno",
        vmin=config.SENSOR_MIN,
        vmax=config.SENSOR_MAX,
    )
    fig.colorbar(sc, label="pressure (some units)")
    return fig, sc

def update_plot(fig, sc, pressure_data):
    """Update the plot with new data and redraw the figure."""
    sc.set_array(pressure_data.reshape(-1))
    fig.canvas.draw()
    fig.canvas.flush_events()

def plot_():
    background_img = plt.imread(config.IMAGE_FILEPATH)
    coordinates = config.IMAGE_COORDINATES[config.IMAGE]

    data = funp.read_lastnlines(config.DATA_FILENAME, config.BUFFER_mean)
    print(data.shape)
    pressure_values = data[:, config.PINS_]   # todo change this so that PINS are associated with a pixel position.

    fig, sc = make_plot(background_img, coordinates, pressure_values)
    # exit the script when the figure is closed
    fig.canvas.mpl_connect("close_event", lambda event: sys.exit())
    plt.show(block=False)

    while True:
        frame_start = time.perf_counter()
        data = funp.read_lastnlines(config.DATA_FILENAME, config.BUFFER_mean)  # returns the mean of last x datapoints
        pressure_values = data[:, config.PINS]  # get the pressure values corresponding to the image

        # update the figure
        update_plot(fig, sc, pressure_values)
        # wait for 0.1s (including the time it took to update the plot)
        frame_time = time.perf_counter() - frame_start
        if frame_time < 0.1:
            plt.pause(0.1 - frame_time)


