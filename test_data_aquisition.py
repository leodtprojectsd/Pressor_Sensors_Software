#!/usr/bin/env python3
'''
live_data_aquisition plots data that it reads iteratively from test_data.txt -
if test_data.txt is live updated, so is the line plot
'''
import time
import random
import os

LIMIT_TIME = 100  # s
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.txt")

def gen_data(filename, limit_time):
    start_time = time.time()
    elapsed_time = time.time() - start_time
    with open(filename, "w") as f:
        while elapsed_time < limit_time:
            f.write(f"{time.time():30.12f} {random.random():30.12f}\n")  # produces 64 bytes
            f.flush()
            elapsed = time.time() - start_time

if __name__ == '__main__':
    gen_data(DATA_FILENAME, LIMIT_TIME)