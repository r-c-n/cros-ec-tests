#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cros.helpers.sysfs import *
import unittest


class TestCrosECPower(unittest.TestCase):
    def test_cros_ec_usbpd_charger_abi(self):
        files = [
            "current_max",
            "input_current_limit",
            "input_voltage_limit",
            "manufacturer",
            "model_name",
            "online",
            "power/autosuspend_delay_ms",
            "status",
            "type",
            "usb_type",
            "voltage_max_design",
            "voltage_now",
        ]
        sysfs_check_attributes_exists(
            self, "/sys/class/power_supply/", "CROS_USBPD_CHARGER", files, False
        )

    def test_cros_ec_battery_abi(self):
        files = [
            "alarm",
            "capacity_level",
            "charge_full_design",
            "current_now",
            "manufacturer",
            "serial_number",
            "type",
            "voltage_min_design",
            "capacity",
            "charge_full",
            "charge_now",
            "cycle_count",
            "model_name",
            "present",
            "status",
            "technology",
            "voltage_now",
        ]
        sysfs_check_attributes_exists(
            self, "/sys/class/power_supply/", "BAT", files, False
        )
