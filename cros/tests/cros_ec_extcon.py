#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.sysfs import *
import unittest


class TestCrosECextcon(unittest.TestCase):
    def test_cros_ec_extcon_usbc_abi(self):
        """ Checks the cros-ec extcon ABI. """
        match = 0
        try:
            for devname in os.listdir("/sys/class/extcon"):
                devtype = read_file("/sys/class/extcon/" + devname + "/name")
                if ".spi:ec@0:extcon@" in devtype:
                    self.assertEqual(
                        os.path.exists("/sys/class/extcon/" + devname + "/state"), 1
                    )
                    for cable in os.listdir("/sys/class/extcon/" + devname):
                        if cable.startswith("cable"):
                            self.assertEqual(
                                os.path.exists(
                                    "/sys/class/extcon/" + devname + "/" + cable + "/name"
                                ),
                                1,
                            )
                            self.assertEqual(
                                os.path.exists(
                                    "/sys/class/extcon/" + devname + "/" + cable + "/state"
                                ),
                                1,
                            )
                            match += 1
        except IOError as e:
            self.skipTest("Exception occured: {0}, skipping".format(e.strerror))
        if match == 0:
            self.skipTest("No extcon device found, skipping")
