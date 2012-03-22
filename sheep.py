#! /usr/bin/env python
# coding=utf-8
"""
sheep.py - Phenny Sheep Module
Copyright 2012, Mark Scala
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import random

def sheep(phenny, input):
    if random.randint(0,1) == 0:
        if input.group(2) != '':
            phenny.say("%s is a sheep!" % (input.group(2)))
        else:
            phenny.say("%s is a sheep!" % (input.nick))
    else:
        if input.group(2) != '':
            phenny.say("%s is a heathen!" % (input.group(2)))
        else:
            phenny.say("%s is a heathen!" % (input.nick))
sheep.commands = ['sheep?']        
        
