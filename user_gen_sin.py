#!/usr/bin/env python3

import numpy as np
import math
from matplotlib import pyplot as plt
import redpitaya_scpi as scpi

IP = '192.168.0.15'
rp_s = scpi.scpi(IP)

wave_form = 'arbitrary'

f_0 = 50  # frequency (Hz)
f_1 = 100  # frequency (Hz)
ampl = 1

buffer = 16384
t0 = np.linspace(0, 1, buffer)*2*np.pi
x0 = np.sin(t0)

# plt.plot(np.arange(len(t0)), x0) #, np.arange(len(t1)), x1)
# plt.title('Custom waveform')
# plt.show()

rp_s.tx_txt('GEN:RST')

# Function for configuring a Source
rp_s.sour_set(1, wave_form, ampl, f_0, data= x0)
rp_s.sour_set(2, wave_form, ampl, f_1, data= x0)

rp_s.tx_txt('OUTPUT:STATE ON')
rp_s.tx_txt('SOUR:TRIG:INT')

rp_s.close()