"""
Acquire and save continuously data from PCB-board.

"""

import time
import os
import csv
import numpy as np
import serial


def connect_to_usb(port="COM3", baudrate=115200, timeout=2,  rx_size=1000000, tx_size=1000000, scale="high"):

    try:
        s = serial.Serial(port, baudrate=baudrate, timeout=timeout)
    except:
        pass
    try:
        s.close()
        s = serial.Serial(port, baudrate=baudrate, timeout=timeout)
    except:
        exit("""Exiting program\n
        serial could not connect, try:\n
        -->disconnecting PCB\n
        --> disconnecting a USB\n
        maybe a serial is open somewhere.""")

    s.set_buffer_size(rx_size=rx_size, tx_size=tx_size)
    print("..Connection successful, is serial port open?: ", s.isOpen())
    s.write(bytearray([30]))  # request connection string
    time.sleep(0.1)
    string = s.read(40)  # read connection string (5 BYTESm "Ready)
    print(list(string))
    if len(string) > 5:
        exit("Connecting string short, try disconnecting and reconnecting PCB and restarting program")
    #set scale
    scale_array = [24, 0, 0, 0, 0] if scale == "high" else [24, 255, 255, 255, 255]
    s.write(bytearray(scale_array))  # checked it works
    print(f"scale set to {scale}")
    time.sleep(1)
    s.write(bytearray([18]))  # start reading
    time.sleep(1)
    print("Data acquisition Started...")
    return s


def get_data_from_USB_PCB(filename, limit_time, scale="high", port="COM3",
                          baudrate=115200, timeout=2, rx_size=1000000, tx_size=1000000):
    """
    Function calls "connect to USB" to connect to external port,
    then reads 62.5Hz of double data (125Hz) for 32 channels, and writes it to file.csv

    :param filename: absolute path.csv
    :param limit_time:  int time before function expires and moves on
    :param scale: "high" or "low" - for setting internal scale & factor multiplication
     - for fun : connect_to_usb
    :param port: "COM3" port to connect to
    :param baudrate: int
    :param timeout: int
    :param rx_size: int
    :param tx_size: int

    :return: nothing - saves data to filename.csv
    """

    factor = 10e5 if scale == "high" else 10e3  # used for resistance calculation
     #connect to serial port
    s = connect_to_usb(port=port,  baudrate=baudrate, timeout=timeout, rx_size=rx_size, tx_size=tx_size, scale=scale)
     #aquire data and write to .csv
    with open(filename, 'w', newline='') as f:
        file_writer = csv.writer(f, delimiter=',')
        start_time = time.time()
        elapsed_time = time.time() - start_time
        while elapsed_time < limit_time:
            bytes_ = list(s.read(131))  # read data
            serial_port_data = np.array(bytes_[1:65] + bytes_[65:-2]).reshape(2, 64)
            got_data = time.time()
             #Tranform Data Bytes --> Resistance
            voltage = (serial_port_data[:, ::2] * 256 + serial_port_data[:, 1::2] + 1) * (
                        2.4 / 2 ** 15)  # https://stackoverflow.com/questions/44068819/copy-every-nth-column-of-a-numpy-array
            resistance = voltage / (2.048 - voltage) * factor  # V to R
            resistance_data = np.insert(resistance, 0,
                                        [got_data - start_time, got_data - start_time + 0.015],
                                        axis=1)  # add the time column as first column

            for data_row in resistance_data: #iterate over each row in data
                file_writer.writerow(data_row)
            f.flush()
            elapsed = time.time() - start_time


if __name__ == '__main__':
    LIMIT_TIME = 100  # s
    DATA_FILENAME = os.path.join(os.getcwd(), "data", "test_data.csv")
    get_data_from_USB_PCB(DATA_FILENAME, LIMIT_TIME, scale="high")
