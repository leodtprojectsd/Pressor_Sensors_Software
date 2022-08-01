


def get_new_vals():
    data = funp.read_lastnlines(config.paths_["DATA_FILENAME"], config.BUFFER_mean)
    if config.FITTING:
        scaler = funp.read_from_pickle(config.paths_["FIT_MINMAX_FILENAME"])
        data[:, 1:] = scaler.transform(data[:, 1:])
    time_ = data[:, 0][0]
    x = config.PINS
    y = data[:, 1:][0]
    y = [y[i] for i in config.PINS - 1]
    return x, y, time_




def data_gen():
    t = data_gen.t
    data = funp.read_lastnlines(config.paths_["DATA_FILENAME"], config.BUFFER_mean)
    t = data[:, 0][0]
    y = data[:, 1:][0]
    yield t, y #yield data but packed in list