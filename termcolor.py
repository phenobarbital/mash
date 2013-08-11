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

@summary: functions to easliy print colored text in terminal
Created on 10/08/2013
@author: Jesus Lara <jesuslarag at gmail.com>
'''

import sys

COLORS = (
    'BLACK', 'RED', 'GREEN', 'YELLOW',
    'BLUE', 'MAGENTA', 'CYAN', 'WHITE'
)

class termcolor(object):
    '''
    Terminal color emulator, print colored text in console terminal (bash, xterm)
    '''
    def has_colors(self):
        '''
        return True if color console is available
        '''
        if (not hasattr(sys.stdout, 'isatty')) or (not (sys.stdout.isatty())): # only on ttys
            return False
        try:
            import curses
            curses.setupterm()
            return curses.tigetnum("colors") > 2
        except:
            return False
    
    def str(self, string, color='WHITE', bold=False):
        '''
        return a colorful console string
        ''' 
        try:
            if self.has_colors():
                if color in COLORS:
                    return '\033[{0};{1}m{2}\033[0m'.format(int(bold), COLORS.index(color) + 30, string)
                else:
                    return string                
        except:
            #guess false, in case of error
            return string

    def __getattr__(self, name):
        '''
        allow use the color name as a function
        '''
        def color(string, bold=True):
            return self.str(string, name.upper(), bold)
        return color

if __name__ == '__main__':
    
    for bold in (False, True):
        for color_name in COLORS:
            print termcolor().str('Example of {0}'.format(color_name), color_name, bold)
    print termcolor().red('red text') + termcolor().blue(' blue text')