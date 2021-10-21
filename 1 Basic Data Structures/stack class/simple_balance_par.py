# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:22:17 2020

@author: virustous
"""

import Stack


def par_checker(symbol_string):
    s = Stack.Stack()
    balanced = True
    for symbol in symbol_string:
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                s.pop()
    
    if balanced and s.is_empty():
        return True
    return False
# end f. par_checker
    

print(par_checker('((()))'))
print(par_checker('(()'))