#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.mcu import *
import fcntl
import unittest


class TestCrosECMCU(unittest.TestCase):
    def test_cros_ec_abi(self):
        """ Checks the standard ABI for the main Embedded Controller. """
        check_mcu_abi(self, "ec")

    def test_cros_fp_abi(self):
        """ Checks the standard ABI for the Fingerprint EC. """
        check_mcu_abi(self, "fp")

    def test_cros_tp_abi(self):
        """ Checks the standard ABI for the Touchpad EC. """
        check_mcu_abi(self, "tp")

    def test_cros_pd_abi(self):
        """ Checks the standard ABI for the Power Delivery EC. """
        check_mcu_abi(self, "pd")

    def test_cros_ec_chardev(self):
        """ Checks the main Embedded controller character device. """
        self.assertEqual(os.path.exists("/dev/cros_ec"), 1)

    def test_cros_ec_hello(self):
        """ Checks basic comunication with the main Embedded controller. """
        fd = open("/dev/cros_ec", "r")
        param = ec_params_hello()
        param.in_data = 0xA0B0C0D0  # magic number that the EC expects on HELLO

        response = ec_response_hello()

        cmd = cros_ec_command()
        cmd.version = 0
        cmd.command = EC_CMD_HELLO
        cmd.insize = sizeof(param)
        cmd.outsize = sizeof(response)

        memmove(addressof(cmd.data), addressof(param), cmd.outsize)
        fcntl.ioctl(fd, EC_DEV_IOCXCMD, cmd)
        memmove(addressof(response), addressof(cmd.data), cmd.insize)

        fd.close()

        self.assertEqual(cmd.result, 0)
        # magic number that the EC answers on HELLO
        self.assertEqual(response.out_data, 0xA1B2C3D4)
