"""
Store all parameters that you may want to change

"""
import numpy as np
import os

# 1. general config
LIMIT_TIME = 100
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")
SCALE = "high"

# 2.  config for real_data_acquisition
PORT = "COM3"
BAUDRATE = 115200
TIMEOUT = 2
RX_SIZE = 1000000
TX_SIZE = 1000000

# 3. config for live_scatter_plot
PINS = np.arange(1, 9)
COLOURS = [f"C{i}" for i in range(1, 33)]
Y_lim = [0, 5e7]
BUFFER_mean = 5  # before plotting scatter, does the mean of this many points

# 4. config for live_matrix_plot
IMAGE = "example_image.png"  # image chosen as background
IMAGE_FILEPATH = os.path.join(os.getcwd(), "background_images", IMAGE)
PINS_ = np.arange(1, 17)  # second time using PINS_ so that you can use a different version for matrix and scatter
IMAGE_COORDINATES = {"example_image.png": [[[462, 106],[547, 113],
                              [430, 156],[601, 237],
                              [543, 222],[497, 221],
                              [430, 216],[444, 266]],
                             [[489, 439],[609, 463],
                              [613, 564],[500, 574],
                              [568, 641],[524, 643],
                              [577, 688],[527, 683]]]}

# min and max values that the sensors will produce
SENSOR_MIN = 0
SENSOR_MAX = 5e7
