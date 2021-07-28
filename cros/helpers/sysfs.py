#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def read_file(name):
    """ Returns the content of the file named 'name'."""
    fd = open(name, "r")
    contents = fd.read()
    fd.close()
    return contents


def sysfs_check_attributes_exists(s, path, name, files, check_devtype):
    """ Checks that all attributes listed in 'files' for a given 'path' exists.
        Note that the 'name' parameter is used to define a pattern to match
        before checking a device path.
    """
    match = 0
    try:
        for devname in os.listdir(path):
            if check_devtype:
                fd = open(path + "/" + devname + "/name", "r")
                devtype = fd.read()
                fd.close()
                if not devtype.startswith(name):
                    continue
            else:
                if not devname.startswith(name):
                    continue
            match += 1
            for filename in files:
                s.assertEqual(os.path.exists(path + "/" + devname + "/" + filename), 1)
    except IOError as e:
            self.skipTest("Exception occured: {0}, skipping".format(e.strerror))
    if match == 0:
        s.skipTest("No " + name + " found, skipping")
