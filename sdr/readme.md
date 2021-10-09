## USE sdr with ddc to get IQ data 

plot_fft.py to plot powerspectrum()

### Recording data with uhd_rx_cfile

uhd_rx_cfile --spec="B:0" -A RX2 -r 2e7 -N 819200 -f 2.e7 test4.bin
