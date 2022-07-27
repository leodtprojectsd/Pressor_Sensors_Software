'''
store functions use in multiple modules

'''
import io
import numpy as np
import pickle
import time


# 1. RETRIVING DATA FROM FILE
def get_data(filename, buffer_len, delay=0.0):
    """
    Establish connection and read the buffer from usb

    :param filename: .txt file
    :param buffer_len: number of bytes to return
    :param delay: float - between different loops
    :return: data as a string
    """
    with open(filename, "r") as f:
        f.seek(0, io.SEEK_END)
        data = f.read(buffer_len)
        if delay:
            time.sleep(delay)
    return data


def read_lastnlines(filename_, n):
    """
    used to read last lines of csv file, used in loop
    :param filename_: csv
    :param n: int - number of lines to return (from bootom)
    :return: n-rows mean, for each column (1,33)
    """
    storage = np.zeros((2, 33))
    with open(filename_) as f:
        for line in (f.readlines()[-n:]):  # read the las n lines
            arr = np.array(line.split(",")).reshape(1, 33)
            storage = np.append(storage, arr, axis=0).astype(float)
    return storage[2:, :].mean(axis=0).reshape(1, 33)


# saving pickle
def save_pickle(filepath_, pickle_object):
    """
    Save an object as pickle (used for fits)
    :param filepath_: where to save to
    :param pickle_object: what to save
    :return: nan
    """

    outfile = open(filepath_, 'wb')
    pickle.dump(pickle_object, outfile)
    outfile.close()
    print(f"pickle saved as {filepath_}")
    return


def read_from_pickle(filename_):
    """
    retrieve pickle objects (used for fits)
    :param filename_ file containing pickled fit:
    :return:scaler object from sklearn min max
    """
    infile = open(filename_, 'rb')
    unpickled = pickle.load(infile)
    infile.close()
    return unpickled
