#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py --- Setup script for mash
# Copyright (c) 2013 Jesus Lara
#
# This file is part of MaSH.
#
# MaSH is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# MaSH is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

PACKAGE = "mash"
VERSION = "0.1.0"

setup(
    name=PACKAGE,
    version=VERSION,
    author='Jesus Lara',
    author_email='jesuslarag@gmail.com',
    description='create interactive shell-commands with python',
    packages = find_packages(exclude = ["tests", "doc"]),
    url = 'https://github.com/phenobarbital/mash',
    license=open('LICENSE').read(),
    platforms="UNIX",
    long_description=open('README.rst').read(),
    keywords=["cmd", "shell", "command", "text-mode interface"],
    py_modules=["mash"]
)
