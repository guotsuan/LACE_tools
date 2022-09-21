#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 gq <gq@lacebian1>
#
# Distributed under terms of the MIT license.

"""
Tek RSA 306 Spectrum get spectrum example
"""

from rsa_api import *
import os

# def spectrum_example():

def get_spectrum_data(cf, span, rbw, avgNum=1):
    print('\n\n########Spectrum Example########')
    search_connect()
    # cf = 2.4453e9
    # cf = 50e6
    refLevel = 0
    # span = 100e6
    # rbw = 10e3
    specSet = config_spectrum(cf, refLevel, span, rbw)
    trace = np.mean(acquire_spectrum(specSet, avgNum=avgNum), axis=0)
    freq = create_frequency_array(specSet)
    peakPower, peakFreq = peak_power_detector(freq, trace)
    return freq, trace, peakFreq, peakPower

def main():
    print('\n\n########Spectrum Example########')
    search_connect()
    # cf = 2.4453e9
    cf = 50e6
    refLevel = 0
    span = 100e6
    rbw = 100e3
    specSet = config_spectrum(cf, refLevel, span, rbw)
    trace = acquire_spectrum(specSet, avgNum=50)
    freq = create_frequency_array(specSet)
    peakPower, peakFreq = peak_power_detector(freq, np.mean(trace, axis=0))

    plt.figure(1, figsize=(10, 7))
    ax = plt.gca()
    ax.plot(freq, np.mean(trace,axis=0), color='b')
    # ax.set_title('Spectrum Trace')
    ax.set_xlabel('Frequency (MHz)')
    ax.set_ylabel('Amplitude (dBm)')
    ax.axvline(peakFreq, alpha=0.5, lw=0.5, color='y')
    ax.text((freq[0] + specSet.span / 20), peakPower,
            'Peak power in spectrum: {:.2f} dBm @ {} MHz'.format(
                peakPower, peakFreq))
    ax.set_xlim([freq[0], freq[-1]])
    ax.set_ylim([refLevel - 100, refLevel])
    ax.set_title("Spectrum")
    plt.tight_layout()

    plt.show()
    rsa.DEVICE_Disconnect()
if __name__ == "__main__":
    os.sched_setaffinity(0, {7,8})
    freq, trace_data,_,_ = get_spectrum_data(100e6, 200e6, rbw=7.32e3, avgNum=50)
    np.savez("spectrum_data.npz", freq=freq, data=trace_data)
