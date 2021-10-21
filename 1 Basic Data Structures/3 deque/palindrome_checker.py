# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:18:34 2021

@author: virustous
"""

import Deque

def pal_checker(s):
    deque = Deque.Deque()
    
    # read string to the deque
    for ch in s:
        deque.addRear(ch)
        
    # check valid palin
    while deque.size() > 1:
        if deque.removeRear() != deque.removeFront():
            return False
    return True
# end f. pal_checker

print(pal_checker('radar'))
print(pal_checker('mama'))
print(pal_checker('reindeer'))
print(pal_checker('reer'))