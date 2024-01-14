#!/usr/bin/env python3

import sys
import redpitaya_scpi as scpi
import matplotlib.pyplot as plot
import numpy as np
from time import sleep
import pandas as pd

import csv

IP = '192.168.0.15'

rp_s = scpi.scpi(IP)

rp_s.tx_txt('ACQ:RST')

rp_s.tx_txt('ACQ:DATA:FORMAT ASCII')
rp_s.tx_txt('ACQ:DATA:UNITS VOLTS')
rp_s.tx_txt('ACQ:DEC 1')
rp_s.tx_txt('ACQ:TRIG:DLY 0')
rp_s.tx_txt('ACQ:TRIG:LEV 0.00')

rp_s.tx_txt('ACQ:START')
rp_s.tx_txt('ACQ:TRIG CH1_PE')
data = []
df = pd.DataFrame(data)

for i in range(5):
    # rp_s.tx_txt('ACQ:START')
    # rp_s.tx_txt('ACQ:TRIG CH1_PE')

    while 1:
        rp_s.tx_txt('ACQ:TRIG:STAT?')
        if rp_s.rx_txt() == 'TD':
            break

    while 1:
        rp_s.tx_txt('ACQ:TRIG:FILL?')
        if rp_s.rx_txt() == '1':
            break

    rp_s.tx_txt('ACQ:SOUR1:DATA:OLD:N? 800')
    # rp_s.tx_txt("ACQ:SOUR1:DATA:Start:N? 0,800")
    # rp_s.tx_txt('ACQ:SOUR1:DATA?')

    buff_string = rp_s.rx_txt()
    buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
    buff = list(map(float, buff_string))
    
    # thresh = 0.00
    arr = np.array(buff)
    # mask1 = (arr[:-1] < thresh) & (arr[1:] > thresh)
    # rising_edge = np.flatnonzero(mask1)+1
    # buff = buff[rising_edge[0]:rising_edge[1]]
    # arr = arr[rising_edge[0]:rising_edge[1]]

    # if len(rising_edge) == 3:
    #     # print(rising_edge)
    #     buff = buff[rising_edge[0]:rising_edge[1]]

    #     plot.plot(buff)
    #     sleep(0.01)
    arr = np.append(1,arr)
    plot.plot(buff)
    # data.append(arr)
    # df.drop(columns=[i for i in check_df.columns])
    df = pd.DataFrame()
    df[str(i)]=pd.Series(arr)
    df.to_csv("data"+str(i)+".csv", index = False, header = False) 
    # np.savetxt("data"+str(i)+".csv", (arr),  fmt='%s' , delimiter=',')

# df.to_csv('data.csv', index = False, header = False) 
# np.savetxt('data.csv', (data),  fmt='%s' , delimiter=',')
plot.ylabel('Voltage')
plot.show()