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
 
@summary: create an interactive shell using cmd and argparse
Created on 10/08/2013
@author: Jesus Lara <jesuslarag at gmail.com>
'''

import cmd
import sys

YES = set(['yes','y', 'YES', 'Y'])
NO = set(['no','n', 'NO', 'N'])

class mShell(cmd.Cmd):
    '''Mandarina: Basic and simple interactive shell
    
    Arguments:
    prompt   default command-prompt symbol
    intro    default message in console mode
    '''

    ruler = '-'
    prompt = '#'
    intro = 'Simple Shell interactive'

    def __init__(self):
        """ Constructor """
        cmd.Cmd.__init__(self)
        self.change_prompt(self.prompt)
    
    def start(self, intro=None):
        return self.cmdloop(intro)

    def cmdloop(self, intro=None):
        """ command loop """
        try:
            return cmd.Cmd.cmdloop(self, self.intro)
        except (KeyboardInterrupt, SystemExit):
            print("^C Exit")
            self.postloop()
    
    def change_prompt(self, line=''):
        """Change the interactive prompt"""
        self.prompt = line + ' > '

    def textinput(self, question, default=''):
        """ Get information via raw_input
        "question" is a string that is presented to the user.
        "default" is default option presented, is the answer if user just hits <Enter>.
        function returns input
        """
        q = question + ': '
        s = raw_input(q)
        return s
        
    def choice(self, question, options=["yes","no"], default='yes'):
        """Ask a question via raw_input() and return their answer.
        "question" is a string that is presented to the user.
        "options" is an dict from options to choice (default: yes, no)
        "default" is the presumed answer if the user just hits <Enter>.
        function returns answer
        """
        prompt = '(' + str.join('|', options) + ')'
        print prompt
        while True:
            sys.stdout.write(question + prompt + ' : ')
            choice = raw_input()
            if default is not None and choice == '':
                return default
            elif choice in options:
                return choice
            else:
                sel = str.join(' or ', options)
                sys.stdout.write('Please respond with "%s"\n' % sel)

    def question(self, question, default='yes'):
        """Ask a question via raw_input() and return their answer.
        "question" is a string that is presented to the user
        "default" is the presumed answer if the user just hits <Enter>.
        function return True for positive answer, false elsewhere
        """
        if default in YES:
            prompt = '(Y|n) : '
        else:
            prompt = '(y|N) : '
        
        while True:
            sys.stdout.write(question + prompt)
            choice = raw_input().lower()
            if default is not None and choice == '':
                return True
            elif choice in YES:
                return True
            elif choice in NO:
                return False
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' \n")
          
    def preloop(self):
        "Hook method executed once when cmdloop() is called"
        # print 'preloop()'
    
    def postloop(self):
        "Hook method executed when cmdloop() is finished"
        print 'Goodbye! ...'
    
    def onecmd(self, s):
        """ override command action """
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        pass
    
    def default(self, line): 
        '''
        Parse string for available commands
        '''
        cmd, arg, line = self.parseline(line)
        # get a complete list of commands
        cmds = self.completenames(cmd)
        n_cmds = len(cmds)
        if n_cmds == 0:
            # no command was found
            print '*** Unknown command "%s"\n' % cmd
        elif n_cmds == 1:
            result = getattr(self, 'do_'+cmds[0])(arg)
            return result
        else:
            # more commands available
            print ' Available commands: %s' % str.join(", ", cmds)

    def do_help(self, arg):
        """ Show this help"""
        doc_strings = [ (i[3:], getattr(self, i).__doc__)
            for i in dir(self) if i.startswith('do_') ]
        doc_strings = [ '  %s\t%s\n' % (i, j)
            for i, j in doc_strings if j is not None ]
        print '\nUsage:\n%s' % ''.join(doc_strings)

    def do_exit(self, line):
        """ Quits the console"""
        return True
    
    def help_exit(self):
        print "Exits Shell"
        print "You can also use the CTRL+D or CTRL+C shortcut."
    
    def do_EOF(self):
        return True
    
    do_quit = do_exit
    help_quit = help_exit
