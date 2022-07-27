#!/usr/bin/env python3
"""
test data aquisition simulates the the data that would be aquired from the DAC.
"""
import time
import os
import csv
import numpy as np

LIMIT_TIME = 100  # s
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")

def gen_data(filename, limit_time):
    with open(filename, 'w', newline='') as f:
        file_writer = csv.writer(f, delimiter=',')
        start_time = time.time()
        elapsed_time = time.time() - start_time
        while elapsed_time < limit_time:
            data = np.random.randint(1, 255, (2, 32)).astype(float)
            now_time = time.time() - start_time # get current time from start to append
            data = (np.insert(data, 0, [now_time,now_time+ 1/62.5], axis=1)).tolist()

            for data_row in data: #iterate over each row in data
                file_writer.writerow(data_row)
            f.flush()
            elapsed = time.time() - start_time
            time.sleep(1/62.5) #what it should be sleeping at

if __name__ == '__main__':
    gen_data(DATA_FILENAME, LIMIT_TIME)