#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helpers.sysfs import *
from helpers.kernel import *
import unittest

class TestCrosECGyro(unittest.TestCase):

    def test_cros_ec_gyro_iio_abi(self):
        files = [ "buffer/", "calibrate", "current_timestamp_clock", "id",
                  "in_anglvel_x_calibbias", "in_anglvel_x_calibscale",
                  "in_anglvel_x_raw", "in_anglvel_y_calibbias",
                  "in_anglvel_y_calibscale", "in_anglvel_y_raw",
                  "in_anglvel_z_calibbias", "in_anglvel_z_calibscale",
                  "in_anglvel_z_raw", "location", "sampling_frequency",
                  "sampling_frequency_available", "scale",
                  "scan_elements/", "trigger/"]
        sysfs_check_attributes_exists( self, "/sys/bus/iio/devices", "cros-ec-gyro", files, True)
        if kernel_greater_than(5,4,0):
            sysfs_check_attributes_exists( self, "/sys/bus/iio/devices", "cros-ec-gyro", ["frequency"], True)
