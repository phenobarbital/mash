#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 Jesus Lara. All rights reserved.
'''
@summary: Class for building command-line programs
Created on 10/08/2013
@author: Jesus Lara <jesuslarag at gmail.com>
@license: LGPL3
'''

from mash import Shell
import subprocess
import sys

class apt(Shell):
    '''Example use of Shell Class, building an interface to apt-get
    '''
    prompt = 'apt'
    intro = "apt command-line demonstration."
    version = '0.1'
    
    def do_install(self, packagelist=[]):
        pkgs = packagelist.split()
        """ Install a package via apt-get """
        args = ['apt-get', 'install', '--yes', '--assume-yes']
        args.extend(pkgs)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        p.wait()
        sys.stdout.writelines(p.stdout.readlines())

if __name__ == '__main__':
    a = apt()
    a.start()