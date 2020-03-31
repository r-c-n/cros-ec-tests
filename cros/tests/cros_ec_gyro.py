#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.kernel import *
from cros.helpers.mcu import *
from cros.helpers.sysfs import *
import unittest


class TestCrosECGyro(unittest.TestCase):
    def test_cros_ec_gyro_iio_abi(self):
        """ Checks the cros-ec gyroscope IIO ABI. """
        files = [
            "buffer/",
            "calibrate",
            "current_timestamp_clock",
            "id",
            "in_anglvel_x_calibbias",
            "in_anglvel_x_calibscale",
            "in_anglvel_x_raw",
            "in_anglvel_y_calibbias",
            "in_anglvel_y_calibscale",
            "in_anglvel_y_raw",
            "in_anglvel_z_calibbias",
            "in_anglvel_z_calibscale",
            "in_anglvel_z_raw",
            "location",
            "sampling_frequency",
            "sampling_frequency_available",
            "scale",
            "scan_elements/",
        ]
        sysfs_check_attributes_exists(
            self, "/sys/bus/iio/devices", "cros-ec-gyro", files, True
        )
        if kernel_greater_than(5, 6, 0):
            if not is_feature_supported(EC_FEATURE_MOTION_SENSE_FIFO):
                sysfs_check_attributes_exists(
                    self, "/sys/bus/iio/devices", "cros-ec-gyro", [
                        "trigger"], True
                )
        else:
            sysfs_check_attributes_exists(
                self, "/sys/bus/iio/devices", "cros-ec-gyro", ["trigger"], True
            )
