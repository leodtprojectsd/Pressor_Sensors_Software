'''
tests combines and runs both programs live_plot and live_data_aquisition,
this enables to detach them and aquire data while simultaneously plottng them.

'''
import config
import live_scatter_plot
import real_data_aquisition
import os
from multiprocessing import Process



if __name__ == '__main__':
    p1 = Process(target=real_data_aquisition.get_data_from_USB_PCB, args=(config.DATA_FILENAME, config.LIMIT_TIME, config.SCALE,
                                                                          config.PORT, config.BAUDRATE, config.TIMEOUT, config.RX_SIZE, config.TX_SIZE ))
    p2 = Process(target=live_scatter_plot.plot_, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()

