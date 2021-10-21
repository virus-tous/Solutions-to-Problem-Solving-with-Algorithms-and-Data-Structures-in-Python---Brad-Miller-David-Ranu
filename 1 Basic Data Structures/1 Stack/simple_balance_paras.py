# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:52:59 2021

@author: virustous
"""

import Stack

def par_checker(string):
    '''check if a string's parentheses appear in a balanced fashion'''
    s = Stack.Stack()
    
    for ch in string:
        if ch == '(':
            s.push(ch)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    return s.isEmpty()
# end f. par_checker

print(par_checker('((()))'))
print(par_checker('(()'))