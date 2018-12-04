from setuptools import setup


#!/usr/bin/env python
#
# Python installation script
# Author - @coderadi

from __future__ import print_function
import os.path
import sys
import setuptools

# Project variables
VER_PROP_FILE = os.path.join(os.path.dirname(__file__), 'version.properties')
REQUIREMENTS_FILE = os.path.join(os.path.dirname(__file__), 'requirements.txt')
CLASSIFIERS = [
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta",
    "Environment :: Plugins",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: Other/Proprietary License",
    "Natural Language :: English",
]


# Read version properties file and extract version number.
def get_version():
    version = "0.1"
    try:
        with open(VER_PROP_FILE) as f:
            for line in f.readlines():
                if line.startswith("version="):
                    version = line.lstrip('version=').strip()
                    break
    except IOError as ioe:
        print(ioe, file=sys.stderr)
    return version


# Read returements.txt file and extract the list of dependency.
def get_install_requirements():
    # read requirements
    requires = []
    try:
        with open(REQUIREMENTS_FILE) as f:
            requires = list(map(lambda l: l.strip(), f.readlines()))
    except IOError as ioe:
        print(ioe, file=sys.stderr)
        sys.exit(1)
    return requires


if __name__ == '__main__':
    setuptools.setup(
        name="ratelimiter",
        version=get_version(),
        description="ratelimiter: Sliding window rate limiter for python.",
        author="coderadi",
        author_email="aditya.verma.connect@gmail.com",
        url="https://github.com/coderadi/ratelimiter",
        keywords=["ratelimiter"],
        install_requires=get_install_requirements(),
        packages=["ratelimiter", ],
        classifiers=CLASSIFIERS,
        long_description="""
            ratelimiter: Sliding window rate limiter for python.
        """,
    )