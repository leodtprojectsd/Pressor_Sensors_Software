'''
stores all functions used from more than one module.

'''
import io
import numpy as np

#1. RETRIVING DATA FROM FILE
def get_data(filename, buffer_len, delay=0.0):
    '''

    :param filename: .txt file
    :param buffer_len: number of bytes to return
    :param delay: float - between different loops
    :return: data as a string
    '''
    with open(filename, "r") as f:
        f.seek(0, io.SEEK_END)
        data = f.read(buffer_len)
        if delay:
            time.sleep(delay)
    return data

def read_lastnlines(filename_,n):
    """
    :param filename_: csv
    :param n: int - number of lines to return (from bootom)
    :return: n-rows mean, for each column (1,33)
    """
    storage = np.zeros((2, 33))
    with open(filename_) as f:
        for line in (f.readlines() [-n:]):
            arr = np.array(line.split(",")).reshape(1,33)
            storage = np.append(storage, arr, axis=0).astype(float)
    return storage[2:, :].mean(axis=0).reshape(1,33)
