"""
Store all parameters that you may want to change

"""
import numpy as np
import os

# general config
LIMIT_TIME = 100
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")
SCALE = "high"

# config for live_scatter_plot
PINS = np.arange(1, 9)
colours = [f"C{i}" for i in range(1, 33)]
Y_lim = [0, 5e7]

# config for real_data_acquisition
PORT = "COM3"
BAUDRATE = 115200
TIMEOUT = 2
RX_SIZE = 1000000
TX_SIZE = 1000000
