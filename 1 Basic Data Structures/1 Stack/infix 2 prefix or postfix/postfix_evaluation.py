# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:54:05 2021

@author: virustous
"""

import Stack

def eval_postfix(postfix):
    '''evaluate a postfix expression'''
    # to store operands
    operandStack = Stack.Stack()
    token_list = postfix.split()
    
    for token in token_list:
        # if token is operand > push on the stack
        if token.isnumeric():
            operandStack.push(int(token))
        # token is operator > pop 2 operands to compute
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()
# end f. eval_postfix

def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2
    raise SyntaxError('Undefined operator!!!')
    
print(eval_postfix('7 8 + 3 2 + /'))
print(eval_postfix('10 3 5 * 16 4 - / +'))