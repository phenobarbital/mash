'''
Created on 11/08/2013

@author: jesuslara
'''
import logging

class log(object):

    def __init__(self):
        '''
        Constructor
        '''
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/temp/myapp.log',
                    filemode='w')
        