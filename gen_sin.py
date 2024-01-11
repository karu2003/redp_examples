#!/usr/bin/env python3

import sys
import redpitaya_scpi as scpi

# wave_form = 'sine'
wave_form = "SQUARE"
freq = 500000
ampl = 1

IP = "192.168.0.15"
rp_s = scpi.scpi(IP)

rp_s.tx_txt('GEN:RST')

# Function for configuring a Source
rp_s.sour_set(1, wave_form, ampl, freq)

# Enable output
rp_s.tx_txt('OUTPUT1:STATE ON')
rp_s.tx_txt('SOUR1:TRIG:INT')

rp_s.close()