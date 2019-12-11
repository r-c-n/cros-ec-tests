#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crostests",
    description="Chromebooks Test Suite",
    version="0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fabien Lahoudere, Enric Balletbo",
    author_email="aragua@collabora.com, enric.balletbo@collabora.com",
    url="https://gitlab.collabora.com/chromiumos/crostests",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: LGPL-2.1-or-later",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Tests",
    ],
)
