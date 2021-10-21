# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:16:52 2021

@author: virustous
"""

import Deque

d = Deque.Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())