#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 gq <gq@imac.lan>
#
# Distributed under terms of the MIT license.

"""
read tiq file
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


from iqtools import *
filename='data.tiq'
dd = TIQData(filename)
dd.read_samples(1024)
ff, pp, _ = dd.get_fft()

matplotlib.use("Qt5Agg")
plt.plot(ff/1e6, 10*np.log10(pp/1e-3))
dd.save_header()
plt.show()

# write_spectrum_to_root(ff, pp, filename, center=dd.center, title='spectrum')

