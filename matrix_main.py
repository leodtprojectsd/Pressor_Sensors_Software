import config
import live_matrix_plot
import real_data_acquisition
from multiprocessing import Process

if __name__ == '__main__':
    p1 = Process(target=real_data_acquisition.get_data_from_USB_PCB,
                 args=(config.DATA_FILENAME, config.LIMIT_TIME, config.SCALE,
                       config.PORT, config.BAUDRATE, config.TIMEOUT, config.RX_SIZE, config.TX_SIZE))
    p2 = Process(target=live_matrix_plot.plot_, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
