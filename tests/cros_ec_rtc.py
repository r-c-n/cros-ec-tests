#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helpers.mcu import *
from helpers.sysfs import *
import unittest

class TestCrosECRTC(unittest.TestCase):
    def test_cros_ec_rtc_abi(self):
        if not is_feature_supported(EC_FEATURE_RTC):
            self.skipTest("EC_FEATURE_RTC not supported, skipping")
        match = 0
        for devname in os.listdir("/sys/class/rtc"):
            fd = open("/sys/class/rtc/" + devname + "/name", 'r')
            devtype = fd.read()
            fd.close()
            if devtype.startswith("cros-ec-rtc"):
                files = [ "date", "hctosys", "max_user_freq", "since_epoch",
                          "time", "wakealarm" ]
                match += 1
                for filename in files:
                    self.assertEqual(os.path.exists("/sys/class/rtc/" + devname + "/" + filename), 1)
        self.assertNotEqual(match,0)
