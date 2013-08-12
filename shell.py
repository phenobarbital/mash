#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 10/08/2013

@author: jesuslara
'''
from mash import mShell
from mash import mCommand
import os
import sys

class shell(mShell, mCommand, object):
    '''
    classdocs
    '''
    prompt = 'shell'
    intro = "Shell command-line demonstration."

    backend = ['dir', 'lvm', 'btrfs']
    filesystem = ['ext3', 'ext4', 'btrfs', 'xfs']
    distribution = ['debian', 'canaima', 'ubuntu']
    network = ['veth', 'macvlan', 'vlan', 'empty']
    
    _use_dhcp = True
    
    role = ''    
    
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
        if callable(func):
            result = getattr(self, self.args.func)(*values)
            return result
        else:
            print "error executing function"

    def do_shell(self, s):
        """ Execute shell commands"""
        os.system(s)
        
    def help_shell(self):
        print "execute shell commands"

    def do_test(self):
        """ Comando de prueba"""
        i = mShell()
        # i.prompt = self.prompt[:-1]+':Test)'
        i.cmdloop()
    
    def do_toto(self):
        """ Comando toto"""
        return self.question('¿Estas casado?:')
        
    # re-defining postloop
    def postloop(self):
        print ' Exit from shell interface'
    
    def do_package(self):
        """ Comando for test textinput """
        print self.textinput('Domain Name')
        
    # set command-line parameters
    
    def _get_network(self, net='veth'):
        """
        specify network option (veth, macvlan, vlan, empty)
        """
        return net
    
    def _get_backend(self, bend='dir'):
        """
        define backend for container storage (default: dir, LVM or btrfs)
        """
        # print backend
        return bend
    
    def _get_hostname(self, hostname):
        """
        get hostname, return None for invalid value
        """
        return hostname
    
    def _get_ip(self, ip):
        """
        get ip address, return None for invalid value
        """
        # print hostname
        return ip    
    
    def _set_role(self, rolename=''):
        """
        role-based script for running in container after creation
        """
        return rolename    

if __name__ == '__main__':
    a = shell()
    a.start()