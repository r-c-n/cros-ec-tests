#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.mcu import *
from cros.helpers.sysfs import *
import unittest
import os

class TestCrosECRTC(unittest.TestCase):
    def test_cros_ec_rtc_abi(self):
        """ Check the cros RTC ABI. """
        if not is_feature_supported(EC_FEATURE_RTC):
            self.skipTest("EC_FEATURE_RTC not supported, skipping")
        match = 0
        try:
            basepath = "/sys/class/rtc"
            for devname in os.listdir(basepath):
                dev_basepath = os.path.join(basepath, devname)
                fd = open(os.path.join(dev_basepath, "name"), "r")
                devtype = fd.read()
                fd.close()
                if devtype.startswith("cros-ec-rtc"):
                    files = [
                        "date",
                        "hctosys",
                        "max_user_freq",
                        "since_epoch",
                        "time",
                        "wakealarm",
                    ]
                    match += 1
                    for filename in files:
                        p = os.path.join(dev_basepath, filename)
                        self.assertTrue(os.path.exists(p), msg=f"{p} not found")
        except IOError as e:
            self.skipTest(f"{e}")
        self.assertNotEqual(match, 0, msg=f"No RTC device found")
