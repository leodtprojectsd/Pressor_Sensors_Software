"""
tests combines and runs both programs live_plot and live_data_acquisition,
this enables to detach them and acquire data while simultaneously plotting them.

"""
import config
import live_scatter_plot
import data_aquistion
from multiprocessing import Process

if __name__ == '__main__':
    p1 = Process(target=data_aquistion.get_data_from_USB_PCB,
                 args=(config.paths_["DATA_FILENAME"], config.LIMIT_TIME, config.SCALE,
                       config.PORT, config.BAUDRATE, config.TIMEOUT, config.RX_SIZE, config.TX_SIZE))
    p2 = Process(target=live_scatter_plot.plot_, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
