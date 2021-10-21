# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:40:40 2020

@author: virustous
"""


import Stack

def dec2bin(dec_number):
    # a stack of remainders
    rem_stack = Stack.Stack()
    
    while dec_number > 0:
        remainder = dec_number % 2
        rem_stack.push(remainder)
        dec_number //= 2
        
    # get the converted by reversing the stack of remainders
    bin_string = ''
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())
        
    return bin_string
# end f. dec2bin
    
print(dec2bin(25))
print(dec2bin(256))
print(dec2bin(26))
