# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:28:53 2020

@author: virustous
"""


import Stack

def matches(opening, closing):
    opens = '{[('
    closes = '}])'
    return opens.index(opening) == closes.index(closing)
# end f. matches
    

def par_checker(symbols):
    s = Stack.Stack()
    balanced = True
    for symbol in symbols:
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
                    break
                
    if balanced and s.is_empty():
        return True
    else:
        return False
# end f. par_checker
        
    
print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
            