# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:21:26 2021

@author: virustous
"""

import Stack

def matches(op, cl):
    '''check type matching'''
    opening = '{[('
    closing = '}])'
    return opening.index(op) == closing.index(cl)

def par_checker(string):
    s = Stack.Stack()
    for ch in string:
        # if ch is an opening, push it to s
        if ch in '{[(':
            s.push(ch)
        # otherwise, ch is a closing
        else:
            if s.isEmpty() or (not matches(s.peek(), ch)):
                return False
            s.pop()
    return s.isEmpty()


print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))