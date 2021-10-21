# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:25:08 2021

@author: virustous
"""

import Stack

def infix2postfix(infix):
    '''convert an infix expression into its postfix form'''
    # declare precedence of operators
    prec = {}
    # '(' has highest precedence, but only remove it when
    # encountering its ')' > set it to lowest val
    prec['('] = 1
    prec['+'] = prec['-'] = 2
    prec['*'] = prec['/'] = 3
    # stack of operators
    opStack = Stack.Stack()
    # resulting postfix
    postfix = []
    token_list = infix.split()
    
    for token in token_list:
        # if token is an operand > simply append to output
        if token.isalnum():
            postfix.append(token)
        # if token is a lef paren > push it on opStack
        elif token == '(':
            opStack.push(token)
        # if token is a right paren > pop all operators from opStack
        # to postfix till reaching its left paren
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = opStack.pop()
        # if token is a operator
        # pop all operators of equal or higher precedence (for L->R operator = left associativity)
        # from opStack to postfix
        # then, push token on opStack
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfix.append(opStack.pop())
            opStack.push(token)
    
    # append remaining operators from opStack to output
    while not opStack.isEmpty():
        postfix.append(opStack.pop())
    
    return ' '.join(postfix)
# end f. infix2postfix


print(infix2postfix(' A * B + C * D '))
print(infix2postfix('A + B * C + D'))
print(infix2postfix('( A + B ) * ( C + D )'))
print(infix2postfix('10 + 3 * 5 / ( 16 - 4 )'))
