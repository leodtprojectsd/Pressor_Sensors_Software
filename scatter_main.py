'''
tests combines and runs both programs live_plot and live_data_aquisition,
this enables to detach them and aquire data while simultaneously plottng them.

'''

import live_scatter_plot
import real_data_aquisition
import os
from multiprocessing import Process

LIMIT_TIME = 100  # s
DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")
SCALE ="high"

if __name__ == '__main__':
    p1 = Process(target=real_data_aquisition.get_data_from_USB_PCB, args=(DATA_FILENAME, LIMIT_TIME))
    p2 = Process(target=live_scatter_plot.plot_, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()

