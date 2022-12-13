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
        self.assertTrue(os.path.exists("/dev/cros_ec"),
                        msg="/dev/ec not found")

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

    def test_cros_fp_reboot(self):
        """ Test reboot command on Fingerprint MCU.

            Coming out of reset, the MCU boot into its RO firmware and
            jumps to the RW version after validate its signature. If the
            protocol used in RO version is different of the RW version, when
            a reboot is issued the AP still uses the protocol version queried
            before transition, this causes the AP to no communicate correctly
            with the RO firmware and thus it doesn't switches to RW firmware.

            This test detects the that situation and reports a failure when
            the embedded controller is not able to transition from RO to RW,
            which is an indication that there is a problem.

            The above issue was fixed with the kernel patch 241a69ae8ea8
            ("platform/chrome: cros_ec: Query EC protocol version if EC
            transitions between RO/RW).
        """
        check_mcu_reboot_rw(self, "cros_fp")
