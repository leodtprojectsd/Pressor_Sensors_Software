import config
import data_aquistion
import live_matrix_plot
import live_scatter_fade

from multiprocessing import Process
import os
import time

if __name__ == '__main__':
    try:
        print(f"Old {config.paths_['DATA_FILENAME']} vesrion found, removing..")
        os.remove(config.paths_["DATA_FILENAME"])  # remove old version of file, if it exists
        print("test.csv removed.")
    except OSError:
        pass

    p1 = Process(target=data_aquistion.get_data_from_USB_PCB,
                 args=(config.paths_["DATA_FILENAME"], config.LIMIT_TIME, config.SCALE,
                       config.PORT, config.BAUDRATE, config.TIMEOUT, config.RX_SIZE, config.TX_SIZE))
    p2 = Process(target=live_scatter_fade.plot_, args=())
    p3 = Process(target=live_matrix_plot.plot_, args=())
    p1.start()
    print ("waiting a bit for data to start a writing..(sleeping 5 seconds)")
    time.sleep(5)

    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

