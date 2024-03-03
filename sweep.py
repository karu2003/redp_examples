#!/usr/bin/env python3

import numpy as np
import math
from matplotlib import pyplot as plt
import redpitaya_scpi as scpi

IP = '192.168.0.15'
rp_s = scpi.scpi(IP)

wave_form = 'arbitrary'


ampl = 1

buffer = 16384
f_min = 200000
f_max = 1000000
duration = 0.001
phi=270
t = np.linspace(0, duration, buffer)
beta = (f_max - f_min) / duration
phase = 2 * np.pi * (f_min * t + 0.5 * beta * t * t)
phi *= np.pi / 180
x0 = np.cos(phase + phi)

# plt.plot(np.arange(len(t)), x0) #, np.arange(len(t1)), x1)
# plt.title('Custom waveform')
# plt.show()

rp_s.tx_txt('GEN:RST')
rp_s.sour_set(1, wave_form, ampl, 1/duration, data= x0)
rp_s.tx_txt('OUTPUT:STATE ON')
rp_s.tx_txt('SOUR:TRIG:INT')
rp_s.close()