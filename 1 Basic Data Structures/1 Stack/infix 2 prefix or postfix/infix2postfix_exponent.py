# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:23:19 2021

@author: virustous
"""

'''
    precedence: ()
                ^ (exponentiation)
                * /
                + -
    associativity:
                    ^: R-L
                    * / + -: L-R
'''

import Stack

def infix2postfix(infix):
    prec = {}
    prec['('] = 1
    prec['+'] = prec['-'] = 2
    prec['*'] = prec['/'] = 3
    prec['^'] = 4
    
    assoc = {}
    assoc['R-L'] = ['^']
    assoc['L-R'] = ['*', '/', '+', '-']
    
    opStack = Stack.Stack()
    token_list = infix.split()
    postfix = []
    
    # scan the infix
    for token in token_list:
        if token.isalnum():
            postfix.append(token)
        elif token == '(' or token == '^':
            opStack.push(token)
        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postfix.append(top)
                top = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfix.append(opStack.pop())
            opStack.push(token)
        
    while not opStack.isEmpty():
        postfix.append(opStack.pop())
    
    return ' '.join(postfix)
# end f. infix2postfix

print(infix2postfix('10 + 3 * 5 / ( 16 - 4 )'))
print(infix2postfix('K + L - M * N + ( O ^ P ) * W / U / V * T + Q'))
print(infix2postfix('K + L - M * N + ( O ^ P ) * W / U / V * T + Q ^ J ^ A'))
print(infix2postfix('A * B ^ C ^ D ^ E ^ F'))
print(infix2postfix('5 * 3 ^ ( 4 - 2 )'))