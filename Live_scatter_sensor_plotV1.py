"""
V1 of live scatter sensor plot is a functioning version of importing data and plotting it (all in one file).

It is relatively slow, but sped up by eliminating past axes with  ax.lines[i].remove()

"""
import numpy as np
import time
import matplotlib.pyplot as plt
import os
import serial
import plotly.express as px
import pandas as pd


 #Values that can be modified
pins = np.arange(1,5) # pass list of pins (as integers) - staring from 1 (since 0 will be taken from time.
DATA_FILENAME = os.path.join(os.getcwd(), "data", "testV1.csv")
scale ="high" #choose "high"- "low"
xlim = 200 #in seconds


#set correct scale
if scale=="high":
    scale_array = [24,0,0,0,0]
    factor = 10e5 #used in coversions
    ylim = 5e7 #set the Resistance plot limit
elif scale == "low":
    scale_array = [24,255,255,255,255]
    factor = 10e3
    ylim = 5e5


#1. ESTABLISH SERIAL PORT CONNECTION - START AQUISTION
print ("Establishing COM3 connection..")
try:
    s = serial.Serial('COM3', baudrate=115200, timeout=2 )
except:
    s.close()
    s = serial.Serial('COM3', baudrate=115200, timeout=2 )

s.set_buffer_size(rx_size = 1000000, tx_size = 1000000)
 #serieal is open
print ("..Connection successful, is serial port open?: ", s.isOpen())

s.write(bytearray([30])) #request connection string
time.sleep(0.1)
string = s.read(40) #read connection string (5 BYTESm "Ready)
print(list(string))

#set scale
s.write(bytearray(scale_array)) #checked it works
print (f"scale set to {scale}")
time.sleep(1)

# 2.  START DATA AQUISITION
s.write(bytearray([18])) #start reading
time.sleep(1)
print ("Data aquisition Started")


#3. AQUIRE AND PLOT DATA OF 32 CHANNELS
# if file exists, remove it
try:
    print("Old test.csv vesrion found, removing..")
    os.remove(DATA_FILENAME) #remove old version of file, if it exists
    print("test.csv removed.")
except OSError:
    pass




start_measurment = time.time()

fig, ax = plt.subplots(1, 1, figsize=(10, 8))
fig.suptitle('Live plot R vs time', fontsize=16)
ax.set_xlabel('time(s)')
ax.set_ylabel('y')
ax.set_ylim([0, ylim])
ax.set_xlim([0, xlim])
plt.show(block=False)
# color each line
colours = [f"C{i}" for i in range(1, 33)]

# extra plot debugging
hz_ = []  # list of speed
time_ = []  # list for time vs Hz plot

# store all data generated
store_data = np.zeros((1, 33))
# only data to plot
to_plot = np.zeros((1, 33))

try:  # , got_data-start_measurment+0.5
    with open(DATA_FILENAME, 'a') as csvfile:
        start_time = time.time()
        counter = 0
        while True:
            counter = counter + 1
            loop_time = time.time()
            # Get data from serial port
            bytes_ = list(s.read(131))  # read data
            serial_port_data = np.array(bytes_[1:65] + bytes_[65:-2]).reshape(2, 64)
            got_data = time.time()
             #Tranform Data Bytes --> Resistance
            Voltage = (serial_port_data[:, ::2] * 256 + serial_port_data[:, 1::2] + 1) * (
                        2.4 / 2 ** 15)  # https://stackoverflow.com/questions/44068819/copy-every-nth-column-of-a-numpy-array
            Resistance = Voltage / (2.048 - Voltage) * factor  # V to R
            Resistance = np.insert(Resistance, 0, [got_data - start_time, got_data - start_time + 0.015],
                                   axis=1)  # add the time column as first column
            store_data = np.append(store_data, Resistance, axis=0)
            to_plot = store_data[-100:, [0] + list(pins)]
            np.savetxt(csvfile, Resistance, delimiter=',', fmt='%s', comments='')
            if counter == 16:  # ? counter to replot every x time
                counter = 0
                for i in range(1, to_plot.shape[1]):
                    ax.plot(to_plot[:, 0], to_plot[:, i], c=colours[i - 1], marker=(5, 2), linewidth=0, label=i)

                    for i in range(len(ax.lines)-30): #removing extra lines this way since ax.lines = ax["lines"].iloc[-33:] not working in pycharm (did in jupternotebook)
                        if i>=0:
                            ax.lines[i].remove()
            ax.legend(list(pins), loc=(1.04, 0))
            fig.canvas.draw()
            fig.canvas.flush_events()
            Hz = 1 / (time.time() - loop_time)
            # for time vs Hz plot
            hz_.append(Hz)
            time_.append(time.time() - start_time)
            print(1 / (time.time() - loop_time), "Hz - frequncy program loops at")

# Catch Keyboard interrupt and Close the port - so you dont have to.
except KeyboardInterrupt:
    print("MEASURMENT INTERRUPTED...")
    print("file size, :", "{:e}".format(os.path.getsize(DATA_FILENAME)))
    s.close()
    print("serial is open: ", s.isOpen())
    pass

print ("making plotly plot..")
# plot data with Plotly - see pins

df = pd.DataFrame(store_data)
df = df[(df > 0).all(1)]
df = df[(df < 50e6).all(1)]
df.iloc[:,1:] = df.iloc[:,1:].rolling(30, min_periods=1).mean()
fig = px.line(df, x=df[0], y=df.columns[pins])
fig.update_layout(
    title="Filtered Plot",
    xaxis_title="time[s]",
    yaxis_title="R[Ω]",
    legend_title="Pins",
    font=dict(
        family="Arial",
        size=18,
        color="Black"
    )
)
fig.show()


