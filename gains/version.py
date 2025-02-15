from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 2
_version_micro = 2  # use '' for first of series, number for 1 and above
_version_extra = 'dev3'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "Genetic Algorithm for Identifying Novel Structures (GAINS)"
# Long description will go up on the pypi page
long_description = """

GAINS
========
GAINS - Genetic Algorithm for Identifying Novel Structures - is a project
that enables molecular design and computational screening of
small molecules--in particular solvents--for energy storage applications.

Built on the molecular functionality of RDKit, future versions of GAINS
should be employable across a spectrum of small-molecule design problems.

To get started using this software, please go to the repository README_.

.. _README: https://github.com/wesleybeckner/gains/blob/master/README.md

License
=======
``gains`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2017--, Wesley Beckner, The University of Washington.
"""

NAME = "gains"
MAINTAINER = "Wesley Beckner"
MAINTAINER_EMAIL = "wesleybeckner@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/wesleybeckner/gains"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Wesley Beckner"
AUTHOR_EMAIL = "wesleybeckner@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'gains': [pjoin('data', '*')]}
REQUIRES = ["numpy"]
