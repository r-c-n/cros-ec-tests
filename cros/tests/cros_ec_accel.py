#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.kernel import *
from cros.helpers.mcu import *
from cros.helpers.sysfs import *
import math
import unittest
import os

class TestCrosECAccel(unittest.TestCase):
    def test_cros_ec_accel_iio_abi(self):
        """ Checks the cros-ec accelerometer IIO ABI. """
        files = [
            "buffer",
            "calibrate",
            "current_timestamp_clock",
            "id",
            "in_accel_x_calibbias",
            "in_accel_x_calibscale",
            "in_accel_x_raw",
            "in_accel_y_calibbias",
            "in_accel_y_calibscale",
            "in_accel_y_raw",
            "in_accel_z_calibbias",
            "in_accel_z_calibscale",
            "in_accel_z_raw",
            "location",
            "sampling_frequency",
            "sampling_frequency_available",
            "scale",
            "scan_elements/",
        ]
        sysfs_check_attributes_exists(
            self, "/sys/bus/iio/devices", "cros-ec-accel", files, True
        )
        if kernel_greater_than(5, 6, 0):
            if not is_feature_supported(EC_FEATURE_MOTION_SENSE_FIFO):
                sysfs_check_attributes_exists(
                    self, "/sys/bus/iio/devices", "cros-ec-accel", [
                        "trigger"], True
                )
        else:
            sysfs_check_attributes_exists(
                self, "/sys/bus/iio/devices", "cros-ec-accel", [
                    "trigger"], True
            )

    def test_cros_ec_accel_iio_data_is_valid(self):
        """ Validates accelerometer data by computing the magnitude. If the
            magnitude is not closed to 1G, that means data are invalid or
            the machine is in movement or there is a earth quake.
        """
        ACCEL_1G_IN_MS2 = 9.8185
        ACCEL_MAG_VALID_OFFSET = 0.25
        match = 0
        try:
            basepath = "/sys/bus/iio/devices"
            for devname in os.listdir(basepath):
                dev_basepath = os.path.join(basepath, devname)
                fd = open(os.path.join(dev_basepath, "name"), "r")
                devtype = fd.read()
                if devtype.startswith("cros-ec-accel"):
                    location = read_file(os.path.join(dev_basepath, "location"))
                    accel_scale = float(read_file(os.path.join(dev_basepath, "scale")))
                    exp = ACCEL_1G_IN_MS2
                    err = exp * ACCEL_MAG_VALID_OFFSET
                    mag = 0
                    for axis in ["in_accel_x_raw",
                                 "in_accel_y_raw",
                                 "in_accel_z_raw"]:
                        axis_path = os.path.join(dev_basepath, axis)
                        value = int(read_file(axis_path))
                        value *= accel_scale
                        mag += value * value
                    mag = math.sqrt(mag)
                    self.assertTrue(abs(mag - exp) <= err,
                                    msg=("Incorrect accelerometer data "
                                         f"in {dev_basepath} ({abs(mag - exp)})"))
                    match += 1
                fd.close()
        except IOError as e:
            self.skipTest(f"{e}")
        if match == 0:
            self.skipTest("No accelerometer found")
