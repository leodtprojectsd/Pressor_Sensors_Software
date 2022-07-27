import config
import live_matrix_plot
import data_aquistion
from multiprocessing import Process

if __name__ == '__main__':
    p1 = Process(target=data_aquistion.get_data_from_USB_PCB,
                 args=(config.paths_["DATA_FILENAME"], config.LIMIT_TIME, config.SCALE,
                       config.PORT, config.BAUDRATE, config.TIMEOUT, config.RX_SIZE, config.TX_SIZE))
    p2 = Process(target=live_matrix_plot.plot_, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
