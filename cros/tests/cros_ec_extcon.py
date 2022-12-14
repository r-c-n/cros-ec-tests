#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.sysfs import *
import unittest
import os

class TestCrosECextcon(unittest.TestCase):
    def test_cros_ec_extcon_usbc_abi(self):
        """ Checks the cros-ec extcon ABI. """
        match = 0
        try:
            basepath = "/sys/class/extcon"
            for devname in os.listdir(basepath):
                dev_basepath = os.path.join(basepath, devname)
                devtype = read_file(os.path.join(dev_basepath, "name"))
                if ".spi:ec@0:extcon@" in devtype:
                    p = os.path.join(dev_basepath, "state")
                    self.assertTrue(os.path.exists(p), msg=f"{p} not found")
                    for cable in os.listdir(dev_basepath):
                        if cable.startswith("cable"):
                            p = os.path.join(dev_basepath, cable, "name")
                            self.assertTrue(os.path.exists(p), msg=f"{p} not found")
                            p = os.path.join(dev_basepath, cable, "state")
                            self.assertTrue(os.path.exists(p), msg=f"{p} not found")
                            match += 1
        except IOError as e:
            self.skipTest(f"{e}")
        if match == 0:
            self.skipTest("No extcon device found")
