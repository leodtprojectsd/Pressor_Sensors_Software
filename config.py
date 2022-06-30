"""
Store all parameters that you may want to change

"""
import numpy as np
import os
import itertools

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
BUFFER_mean = 20  # before plotting scatter, does the mean of this many points
pin_color = {1: '#e6194b', 2: '#3cb44b', 3: '#ffe119', 4: '#4363d8', 5: '#f58231',
             6: '#911eb4', 7: '#46f0f0', 8: '#f032e6', 9: '#bcf60c', 10: '#fabebe',
             11: '#008080', 12: '#e6beff', 13: '#9a6324', 14: '#fffac8', 15: '#800000',
             16: '#aaffc3'}
marker = [',', '+', '.', 'o', '*',',', '+', '.', 'o', '*',',', '+', '.', 'o', '*',',', '+', '.', 'o', '*']
# 4. config for live_matrix_plot
IMAGE = "example_image_.png"  # image chosen as background
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

IMAGE_COORDINATES = {"example_image_.png":
                         [[[134, 757],[193,762],
                              [134, 715],[186,710],
                              [107, 629],[254,620],
                              [230, 496],[92.6, 475]],
                             [[40.8,273],[25.3, 218],
                              [102,223],[155,224],
                              [219, 240],[28,148],
                              [161.7, 99.7],[59,87]]]}

# min and max values that the sensors will produce
SENSOR_MIN = 0
SENSOR_MAX = 5e7

