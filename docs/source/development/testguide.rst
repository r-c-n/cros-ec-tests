******************
Testing Guidelines
******************

This section describes the testing framework and format standards for tests in
``cros-ec-tests`` packages.

Testing Framework
*****************

The testing framework used by ``cros-ec-tests``  is the `unittest`_ framework.

.. _unittest: https://docs.python.org/3/library/unittest.html

Running Tests
*************

The first thing you should do is download latest source version::

    git clone git://git.kernel.org/pub/scm/linux/kernel/git/chrome-platform/cros-ec-tests.git
    cd cros-ec-tests

At the root of the project, add the current directory in the PYTHONPATH::

    export PYTHONPATH=${PYTHONPATH}:${PWD}

There are currently different ways to invoke ``cros-ec-tests``. Each method
invokes `unittest`_ to run the tests but offers different options when
calling. To run the tests, you will need to make sure you have the `unittest`_
package is installed.

Using a runner
==============

This is the simplest way to run all the tests, just start a runner with::

    python3 -m cros.runners.lava_runner

Using the unittest Command-Line Interface
=========================================

The unittest module can be used from the command line to run tests from
modules::

    python3 -m unittest cros.tests.cros_ec_rtc

You can run tests with more detail (higher verbosity) by passing in the -v flag::

    python3 -m unittest -v cros.tests.cros_ec_rtc

Writing tests
*************

Simple example
==============

The following example shows a simple function and a test to test this
function::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import unittest

    def func(x):
        """Add one to the argument."""
        return x + 1

    class TestSimple(unittest.TestCase):
        def test_answer(self):
            """Check the return value of func() for an example argument."""
            self.assertEqual(func(3), 5)

If we place this in ``cros/tests/example.py`` file and then run::

    python3 -m unittest cros.tests.example

The result is::

    F
    ======================================================================
    FAIL: test_answer (cros.tests.example.TestSimple)
    Check the return value of func() for an example argument.
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "~/cros-ec-tests/cros/tests/example.py", line 13, in test_answer
          self.assertEqual(func(3), 5)
    AssertionError: 4 != 5

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (failures=1)

Where to put tests
==================

Package-specific tests
----------------------

Each package should include a suite of unit tests, covering as many of
the public methods/functions as possible. These tests should be
included inside each sub-package, e.g::

    cros/tests/

``tests`` directories should contain an ``__init__.py`` file so that
the tests can be imported and so that they can use relative imports.

Regression tests
================

One of the main focus of this framework is catch kernel regressions on
future releases using KernelCI. Any time a kernel bug is fixed, and
wherever possible, one or more regression tests should be added to ensure
that the bug is not introduced in future. Regression tests should include
a description of the reported bug.

