import config
import live_line_plot
import data_aquistion
from multiprocessing import Process
import os
import time

if __name__ == '__main__':
    try:
        print(f"Old {config.paths_['DATA_FILENAME']} version found, removing..")
        os.remove(config.paths_['DATA_FILENAME'])  # remove old version of file, if it exists
        print("file.csv removed.")
    except OSError:
        pass

    p1 = Process(target=data_aquistion.get_data_from_USB_PCB,
                 args=(config.paths_['DATA_FILENAME'], config.LIMIT_TIME, config.SCALE,
                       config.PORT, config.BAUDRATE, config.TIMEOUT, config.RX_SIZE, config.TX_SIZE))
    p2 = Process(target=live_line_plot.plot_, args=())
    p1.start()
    time.sleep(6)
    print("waiting a bit for data to start a writing..(sleeping 5 seconds)")
    p2.start()
    p1.join()
    p2.join()
