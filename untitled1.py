# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:39:26 2024

@author: User
"""

class Greeter(object):
    
    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
        print('Hello %s' % self.name.upper())

g = Greeter('Fred')
g.greet(loud=True)
