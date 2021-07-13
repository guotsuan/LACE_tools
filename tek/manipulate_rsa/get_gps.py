#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the MIT license.

"""
get the gps data

"""

def get_gps_data(port='COM3', bandrate=9600, timeout=1):

    import serial, pynmea2
    try:
        ser = serial.Serial('COM3', 9600, timeout=1)

        if not ser.is_open:
            ser.open()

        get_data = False

        while not get_data:
            line = ser.readline()
            if b'$GNGGA' in line:
                gps=pynmea2.parse(line.decode())
                get_data=True

        ser.close()
        return gps

    except Exception as e:
        print("Exception: No communiaton port is found, skipping location")
        return None


def dump_gps_data(fn, gps):
    import numpy as np
    import json

    if gps is not None:
        data={}
        fields = ['longitude', 'latitude', 'altitude']
        data['longitude'] = gps.longitude
        data['latitude'] = gps.latitude
        data['altitude'] = gps.altitude

        out = json.dumps(data)

        f = open(fn,"w")
        f.write(out)
        f.close()
    else:
        print("No GPS logged")

if __name__ == '__main__':
    gps = get_gps_data()
    dump_gps_data("test.json", gps)
    if gps is not None:
        print(gps.longitude, gps.latitude)

