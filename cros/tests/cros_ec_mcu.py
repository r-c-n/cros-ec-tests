#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.mcu import *
import fcntl
import unittest


class TestCrosECMCU(unittest.TestCase):
    def test_cros_ec_abi(self):
        """ Checks the standard ABI for the main Embedded Controller. """
        check_mcu_abi(self, "cros_ec")

    def test_cros_fp_abi(self):
        """ Checks the standard ABI for the Fingerprint EC. """
        check_mcu_abi(self, "cros_fp")

    def test_cros_tp_abi(self):
        """ Checks the standard ABI for the Touchpad EC. """
        check_mcu_abi(self, "cros_tp")

    def test_cros_pd_abi(self):
        """ Checks the standard ABI for the Power Delivery EC. """
        check_mcu_abi(self, "cros_pd")

    def test_cros_ec_chardev(self):
        """ Checks the main Embedded controller character device. """
        self.assertEqual(os.path.exists("/dev/cros_ec"), 1)

    def test_cros_ec_hello(self):
        """ Checks basic comunication with the main Embedded controller. """
        mcu_hello(self, "cros_ec")

    def test_cros_fp_hello(self):
        """ Checks basic comunication with the fingerprint controller. """
        mcu_hello(self, "cros_fp")

    def test_cros_tp_hello(self):
        """ Checks basic comunication with the touchpad controller. """
        mcu_hello(self, "cros_tp")

    def test_cros_pd_hello(self):
        """ Checks basic comunication with the power delivery controller. """
        mcu_hello(self, "cros_pd")
