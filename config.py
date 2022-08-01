"""
Store all parameters that you may want to change

"""
import numpy as np
import os



# 1. genereal settings
LIMIT_TIME = 100
FITTING = False # specify if you are going to fit with min-max scalar #todo make linear regression albinometer
IMAGE = "R1_L2_EXAMPLE"  # image chosen as background (see paths_ for all options)
SCALE = "high" #interal parameter of PCB

paths_ = {
    "DATA_FILENAME": os.path.join(os.getcwd(), "data", "test_data.csv"), # data from usb is saved here
    "WEIGHT_FILENAME": os.path.join(os.getcwd(), "data", "weight_data.csv"),  # data from arudino usb  is saved here
    "COMBINED_FILENAME": os.path.join(os.getcwd(), "data", "combined_data.csv"),  # arduino + pcb

    "FIT_MINMAX_FILENAME": os.path.join(os.getcwd(), "fits", "Fit_minmax"), #data of min max scaler fit is saved here

      #Background images for plots
    "L1_R1_hand": os.path.join(os.getcwd(), "background_images", "L1_R1_Hand.png"),
    "R1_L2_EXAMPLE": os.path.join(os.getcwd(), "background_images", "R1_L2_EXAMPLE.png"),
    "L2_R2_Hand": os.path.join(os.getcwd(), "background_images", "L2_R2_Hand.png"),
    "L1_R1_Hand": os.path.join(os.getcwd(), "background_images", "L1_R1_Hand.png")
}
 # 2.  config for data_aquistion
PORT = "COM3"
BAUDRATE = 115200
TIMEOUT = 2
RX_SIZE = 1000000
TX_SIZE = 1000000

#3. PLOT CONIFIGURE
PINS = np.arange(1, 17) #list of plots you want to see
marker = [',', '+', '.', 'o', '*',',', '+', '.', 'o', '*',',', '+', '.', 'o', '*',',', '+', '.', 'o', '*']

# 3a config for live_scatter_plot
COLOURS = [f"C{i}" for i in range(1, 33)]
Y_lim = [0, 0.5e7]
BUFFER_mean = 20  # before plotting scatter, does the mean of this many points
pin_color = {1: '#e6194b', 2: '#3cb44b', 3: '#ffe119', 4: '#4363d8', 5: '#f58231',
             6: '#911eb4', 7: '#46f0f0', 8: '#f032e6', 9: '#bcf60c', 10: '#fabebe',
             11: '#008080', 12: '#e6beff', 13: '#9a6324', 14: '#fffac8', 15: '#800000',
             16: '#aaffc3'}

 #3b. config for scatter fadde using colurs for scatter fade, after first 17 colours probably doesn't fade
colors_fade = [
    'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
    'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
    'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
    'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
    'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
    'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'
            ]

 # 3c. config for live_matrix_plot
IMAGE_COORDINATES = {"example_image":
                         [[[462, 106],[547, 113],
                           [430, 156],[601, 237],
                           [543, 222],[497, 221],
                           [430, 216],[444, 266]],
                           [[489, 439],[609, 463],
                           [613, 564],[500, 574],
                           [568, 641],[524, 643],
                           [577, 688],[527, 683]]],

                     "example_image_":
                         [[[134, 757],[193,762],
                           [134, 715],[186,710],
                           [107, 629],[254,620],
                           [230, 496],[92.6, 475]],
                           [[40.8,273],[25.3, 218],
                           [102,223],[155,224],
                           [219, 240],[28,148],
                           [161.7, 99.7],[59,87]]],
                     "R1_L2_EXAMPLE":
                         [[[624,1072],[680, 1071],
                           [595, 734], [544, 475],
                           [635, 379], [539, 274],
                           [714, 385], [745,738]],
                           [[222, 772],[258,468],
                           [405,323],[359,455],
                           [437, 528],[416,759],
                           [394, 1098],[325,1107]]],
                     "L2_R2_Hand":
                         [[[503,251],[413, 155],
                           [293, 343], [305, 99],
                           [198, 460], [175, 217],
                           [148, 136], [61,381]],
                           [[500, 300],[667,242],
                           [764,148],[865,335],
                           [863, 118],[700,400],
                           [964, 241],[1103,398]]],
                     "L1_R1_Hand":
                         [[[503,244],[360, 333],
                           [435, 136], [305, 99],
                           [269, 511], [201, 235],
                           [190, 163], [59,449]],
                           [[735, 238],[849,136],
                           [958,371],[968,125],
                           [1093, 271],[1106,177],
                           [1010, 530],[1193,497]]]
                     }

 #3c line plot
line_plot_xlim = (0, 200)
line_plot_ylim = (0, 5e7)
# min and max values that the sensors will produce
SENSOR_MIN = 0
SENSOR_MAX = 1e7
alpha_matrix = 1 #change the transparency


