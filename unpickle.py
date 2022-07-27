import os
import pickle
import pandas as pd
import config


def read_from_pickle (filename_):
    infile = open(filename_, 'rb')
    unpickled = pickle.load(infile)
    infile.close()
    return unpickled

if __name__ == '__main__':
    DATA_FILENAME = config.paths_["DATA_FILENAME"]
    fit_filename = config.paths_["FIT_MINMAX_FILENAME"]
    scaler = read_from_pickle(fit_filename)
    df = pd.read_csv(DATA_FILENAME)
    X = df.iloc[:, 1:]
    df_scaled = scaler.transform(X)
    print(df.min(axis=0), df.max(axis=0), df_scaled.min(axis=0), df_scaled.max(axis=0), sep = "\n")


