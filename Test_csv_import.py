import functions_pressure as funp
import os
import io
import time
import pandas as pd

BUFFER_LEN = 64
PLOT_LIMIT = 20
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")
verbose = False
# df = pd.read_csv(DATA_FILENAME)


with open(DATA_FILENAME, "r") as f:
    print(io.SEEK_END)
    print (f.seek(0, io.SEEK_END))
    data = f.read(BUFFER_LEN)
    print (f)
