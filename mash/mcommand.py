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
 
@summary: create automatically command-line arguments
Created on 10/08/2013
@author: Jesus Lara <jesuslarag at gmail.com>
'''

import argparse

class mCommand(object):
    '''
    Mandarina: create a command-line program, with command-line arguments
    
    Arguments:
    
    intro     description in command usage
    args      command-line arguments parsed
    '''
    intro = "a command-line arguments auto-parse"
    version = '0.1.0'
    
    args = []

    def __init__(self):
        '''
        Constructor
        '''
        self.parser = argparse.ArgumentParser(description = self.intro, conflict_handler='resolve')
        self.build_arguments()
        self.default_arguments()
        # build commands
        self.build_commands()

    def default_arguments(self):
        # version
        self.parser.add_argument('-v','--version', action='version', version=self.version)
        
    def build_arguments(self):
        """
        generate all arguments from functions with "_get_" prefix
        """
        for i in dir(self):
            func = getattr(self, i)
            h = ''
            if i.startswith('_get_'):
                # function return a string, validate with function
                name = func.__name__.replace('_get_', '')
                print name
                if func.__doc__ is not None:
                    h = func.__doc__.strip(' \t\n\r')
                arg = '--'+name
                if hasattr(self, name):
                    # is a choice method
                    c = getattr(self, name)
                    meta = str.join('|', c)
                    default = c[0]
                    self.parser.add_argument(arg, help=h, type=func, metavar=meta, choices=c, nargs=1, action='store', default=default)
                else:
                    self.parser.add_argument(arg, help=h, type=func, metavar=name, nargs=1, action='store')
            if i.startswith('_use_'):
                # is an attribute, define a boolean value, without arguments
                name = i.replace('_use_', '')
                h = i.replace('_', ' ').capitalize()
                arg = '--'+name
                self.parser.add_argument(arg, help=h, action='store_true', default=False)
            if i.startswith('_set_'):
                # is a function with multiple append values, use action='append'
                name = func.__name__.replace('_set_', '')
                if func.__doc__ is not None:
                    h = func.__doc__.strip(' \t\n\r')
                arg = '--'+name
                self.parser.add_argument(arg, help=h, metavar=name, nargs = "+", action='append', type=func)
        
    def add_argument(self, option, group=None, action='store'):
        """ add a simple argument to command line-parser """
        name, h = option
        meta = name.replace('--','')
        if group is not None:
            group.add_argument(name, help=h, metavar=meta, nargs = "?", action=action)
        else:
            self.parser.add_argument(name, help=h, metavar=meta, nargs = "?", action=action)

    def add_argument_group(self, group, description = ''):
        """ add a argument group to command line-parser, return group """
        try:
            return self.parser.add_argument_group(group, description)
        except:
            return False
        
    def parse_args(self):
        self.args = self.parser.parse_args()
        return self.args
    
    def build_commands(self):
        notparse = ['do_EOF', 'do_exit', 'do_quit', 'do_help']
        commands = [ (i[3:], getattr(self, i)) for i in dir(self) if (i.startswith('do_') and not (i in notparse)) ]
        if len(commands):
            self.subparser = self.parser.add_subparsers(title='Available Commands')
            for name, func in commands:
                h = ''
                if func.__doc__ is not None:
                    h = func.__doc__
                a = self.subparser.add_parser(name, help=h)
                a.add_argument('value', nargs='?')
                a.set_defaults(func='do_'+name)