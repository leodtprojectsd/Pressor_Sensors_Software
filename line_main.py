import config
import live_line_plot
import real_data_acquisition
from multiprocessing import Process
import os

if __name__ == '__main__':
    try:
        print(f"Old {config.DATA_FILENAME} vesrion found, removing..")
        os.remove(config.DATA_FILENAME)  # remove old version of file, if it exists
        print("test.csv removed.")
    except OSError:
        pass

    p1 = Process(target=real_data_acquisition.get_data_from_USB_PCB,
                 args=(config.DATA_FILENAME, config.LIMIT_TIME, config.SCALE,
                       config.PORT, config.BAUDRATE, config.TIMEOUT, config.RX_SIZE, config.TX_SIZE))
    p2 = Process(target=live_line_plot.plot_, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
