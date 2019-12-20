#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Return an int froom kernel version to allow to compare
def version_to_int(version, major, minor):
    pattern = "{0:03d}{1:03d}{2:03d}"
    return int(pattern.format(version, major, minor))


# Return the running kernel version
def current_kernel_version():
    fd = open("/proc/version", "r")
    current = fd.read().split()[2].split("-")[0].split(".")
    fd.close()
    return version_to_int(int(current[0]), int(current[1]), int(current[2]))


def kernel_lower_than(version, major, minor):
    if version_to_int(version, major, minor) > current_kernel_version():
        return True
    return False


def kernel_greater_than(version, major, minor):
    if version_to_int(version, major, minor) < current_kernel_version():
        return True
    return False
