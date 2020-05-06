# -*- coding: utf-8 -*-

import os
import configparser

config = configparser.ConfigParser()
network_config = configparser.ConfigParser()

config.read(os.environ['PYTHONPATH'] + '/config.ini')
network_config.read(os.environ['PYTHONPATH'] + '/network.ini')
