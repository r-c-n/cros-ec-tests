#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def version_to_int(version, major, minor):
    """ Return an integer from kernel version to allow to compare with
        others.
    """
    pattern = "{0:03d}{1:03d}{2:03d}"
    return int(pattern.format(version, major, minor))


def current_kernel_version():
    """ Returns the current kernel version as an integer you can
        compare.
    """
    fd = open("/proc/version", "r")
    current = fd.read().split()[2].split("-")[0].split(".")
    fd.close()
    return version_to_int(int(current[0]), int(current[1]), int(current[2]))


def kernel_lower_than(version, major, minor):
    """ Returns true if the given version is lower than the running kernel
        version.
    """
    if version_to_int(version, major, minor) > current_kernel_version():
        return True
    return False


def kernel_greater_than(version, major, minor):
    """ Returns true if the given version is greater than the running kernel
        version.
    """
    if version_to_int(version, major, minor) < current_kernel_version():
        return True
    return False
