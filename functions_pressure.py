'''
stores all functions used from more than one module.

'''
import io


def get_data(filename, buffer_len, delay=0.0):
    with open(filename, "r") as f:
        f.seek(0, io.SEEK_END)
        data = f.read(buffer_len)
        if delay:
            time.sleep(delay)
    return data