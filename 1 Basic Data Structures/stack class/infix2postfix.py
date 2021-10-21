# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:19:38 2020

@author: virustous
"""


import Stack
import string

def infix2postfix(infix_expr):
    '''convert infix expression to postfix'''
    prec = {}
    prec['*'] = prec['/'] = 3
    prec['+'] = prec['-'] = 2
    prec['('] = 1
    
    op_stack = Stack.Stack()
    postfix_list = []
    token_list = infix_expr.split()
    
    for token in token_list:
        if token in string.ascii_uppercase or token in '0123456789':
            