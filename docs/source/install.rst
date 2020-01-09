************
Installation
************

Requirements
============

``cros-ec-tests`` has the following strict requirements:

- `Python <https://www.python.org/>`_ 3.5 or later

- `unittest2 <https://docs.python.org/3/library/unittest.html>`_ 1.1.0 or later

Installing ``cros-ec-tests``
========================

To install ``cros-ec-tests`` with `pip <https://pip.pypa.io>`_, run::

    pip install git+https://gitlab.collabora.com/chromiumos/cros-ec-tests.git

Testing an Installed ``cros-ec-tests``
----------------------------------

The easiest way to test if your installed version of ``cros-ec-tests`` is running
correctly is to use one of the runner function::

    python3 -m cros.runners.lava_runner

The tests should run and print out the result.

Building Documentation
----------------------

Dependencies
^^^^^^^^^^^^

Building the documentation requires the ``cros-ec-tests`` source code and some
additional packages. The easiest way to install the extra dependencies for
documentation is to install the distribution packages:

* `Sphinx <http://www.sphinx-doc.org/>`_ - the main package we use to build
  the documentation
* `python3-sphinx-rtd-theme <https://github.com/readthedocs/sphinx_rtd_theme>`_ -
  the default 'bootstrap' theme used by ``cros-ec-tests``

Building
^^^^^^^^

The easy way is to execute the command (from the ``cros-ec-tests`` source
directory)::

    cd docs
    make html

The documentation will be built in the ``docs/build/html`` directory, and can
be read by pointing a web browser to ``docs/build/html/index.html``.

