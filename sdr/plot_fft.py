#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 gq <gq@gqhp>
#
# Distributed under terms of the MIT license.

"""

"""
import iqtools
import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('Qt5Agg')

center = 2.e7
filename = './test4.bin'
iqdata = iqtools.GRData(filename, fs = 4.e7, center=2.e7)
iqdata.read_complete_file()
xx, yy, _ = iqdata.get_fft(nframes=100, lframes=8192)
plt.plot(xx + 2.e7 ,np.log10(yy))
plt.show()
# xx, yy, zz = iqdata.get_spectrogram(nframes=2000, lframes=1024)
# iqtools.plot_spectrogram(xx, yy, zz)
