#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 Jesus Lara. All rights reserved.
 
'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
 
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

@summary: Class for building command-line programs
Created on 10/08/2013
@author: Jesus Lara <jesuslarag at gmail.com>
'''

from mshell import mShell
from mcommand import mCommand
import sys

class Shell(mShell, mCommand):
    ''' Build an interactive, command-line program
    '''
    
    intro = "Shell command-line demonstration."
    
    def __init__(self):
        mShell.__init__(self)
        mCommand.__init__(self)
        
    def start(self):
        if not len(sys.argv) > 1:
            # starts console mode
            self.cmdloop()
        else:
            self.parse_args()
            # processing commands
            self.arg_process()

    def arg_process(self):
        func = getattr(self, self.args.func)
        if self.args.value is not None:
            values = self.args.value.split(',')
        else:
            values = []
        # process command
        try:
            if callable(func):
                return getattr(self, self.args.func)(*values)
        except:
            return False
    
    # re-defining postloop
    def postloop(self):
        print ' Exit from shell interface'