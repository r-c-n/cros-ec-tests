#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helpers.sysfs import *
from helpers.kernel import *
import math
import unittest

class TestCrosECAccel(unittest.TestCase):

    def test_cros_ec_accel_iio_abi(self):
        files = [ "buffer", "calibrate", "current_timestamp_clock", "id",
                  "in_accel_x_calibbias", "in_accel_x_calibscale",
                  "in_accel_x_raw", "in_accel_y_calibbias",
                  "in_accel_y_calibscale", "in_accel_y_raw",
                  "in_accel_z_calibbias", "in_accel_z_calibscale",
                  "in_accel_z_raw", "location", "sampling_frequency",
                  "sampling_frequency_available", "scale",
                  "scan_elements/", "trigger/"]
        sysfs_check_attributes_exists( self, "/sys/bus/iio/devices", "cros-ec-accel", files, True)
        if kernel_greater_than(5,4,0):
            sysfs_check_attributes_exists( self, "/sys/bus/iio/devices", "cros-ec-accel", ["frequency"], True)


    # This function validate accelerometer data by computing the magnitude.
    # If the magnitude is not closed to 1G, that means data are invalid or
    # the machine is in movement or there is a earth quake.
    def test_cros_ec_accel_iio_data_is_valid(self):
        ACCEL_1G_IN_MS2 = 9.8185
        ACCEL_MAG_VALID_OFFSET = .25
        match = 0
        for devname in os.listdir("/sys/bus/iio/devices"):
            base_path = "/sys/bus/iio/devices/" + devname + "/"
            fd = open(base_path + "name", 'r')
            devtype = fd.read()
            if devtype.startswith("cros-ec-accel"):
                location = read_file(base_path + "location")
                accel_scale = float(read_file(base_path + "scale"))
                exp = ACCEL_1G_IN_MS2
                err = exp * ACCEL_MAG_VALID_OFFSET
                mag = 0
                for axis in ['x', 'y', 'z']:
                    axis_path = base_path + "in_accel_" + axis + "_raw"
                    value = int(read_file(axis_path))
                    value *= accel_scale
                    mag += value * value
                mag = math.sqrt(mag)
                self.assertTrue(abs(mag - exp) <= err)
                match += 1
            fd.close()
        if match == 0:
            self.skipTest("No accelerometer found, skipping")

