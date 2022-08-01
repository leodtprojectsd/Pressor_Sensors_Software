#imports for Serial data
import serial
import time
import numpy as np
import config
import csv

weights = []
times = []




def connect_arduino_to_usb (port ="COM6", baudrate_arduino=9600, timeout=2):
    try:
        ser = serial.Serial('COM6', baudrate=baudrate_arduino, timeout=timeout)  # change to config port
    except:
        pass
    try:
        print("not connecting, trying to close and re-open..")
        ser.close()
        ser = serial.Serial('COM6', baudrate=baudrate_arduino, timeout=timeout)   # change to config port
    except:
        exit("""
        Exiting program\n
        serial could not connect to arduino  
        """)
    return (ser)



def get_data_from_USB_Arduino(filename,  port="COM6", baudrate=9600, timeout=2):
    ser = connect_arduino_to_usb()
    with open (filename, 'w', newline='') as f:
        file_writer = csv.writer(f, delimiter=',')
        start_time = time.time() #todo make this match the data aquisiton (dont use start time but absoloute)
        try:
            while True:  # read data infinite
                line = ser.readline()  # read a byte string
                if line:

                    weight_ = float((line.decode()).split()[1])/1000 # weight in Kg
                    time_ = time.time()
                    data = np.array([time_, weight_])

                    file_writer.writerow(data)
                    f.flush()

        except KeyboardInterrupt:
            print("MEASURMENT INTERRUPTED...")
            ser.close()





get_data_from_USB_Arduino(filename=config.paths_["WEIGHT_FILENAME"])


