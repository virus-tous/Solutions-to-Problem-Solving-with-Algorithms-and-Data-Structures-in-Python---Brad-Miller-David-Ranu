# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:00:15 2021

@author: virustous
"""

from Stack import Stack
from par_checker import par_checker

'''
1. Modify the infix-2-postfix algorithm so that it can handle errors.
'''


def validateInput(infix):
    '''check if input is valid.
    if so, return valid input,
    unbalanced parentheses > F,
    infix contains invalid token other than operators and 
    operands > F
    '''
    infix = infix.strip()
    tokenList = infix.split()
    operators = ['^', '*', '/', '+', '-']
    # check if characters are valid
    for c in tokenList:
        if (c not in operators) and (not c.isalnum()) and (c not in ('(', ')')):
            return False
    # check if parens are balanced
    parens = ''
    for c in tokenList:
        if c in ('(', ')'):
            parens += c
    return par_checker(parens)


def infix2postfix(infix):
    '''convert an infix to its postfix'''
    # validate infix expression
    if not validateInput(infix):
        raise Exception('Invalid Infix Expression!')
        
    prec = {}
    prec['('] = 1
    prec['+'] = prec['-'] = 2
    prec['*'] = prec['/'] = 3
    prec['^'] = 4
    tokenList = infix.split()   # convert infix to list of tokens
    postfix = []    # resulting output
    opStack = Stack()   # holding operators
    # scan the token list
    for c in tokenList:
        # if c is an operand, append to output
        if c.isalnum():
            postfix.append(c)
        # if c is left paren or ^, push it on opStack
        elif c == '(' or c == '^':
            opStack.push(c)
        # if c is right paren, move all operators from opStack to output
        # till removing its associated left paren
        elif c == ')':
            top = opStack.pop()
            while top != '(':
                postfix.append(top)
                top = opStack.pop()
        # if c is an operator, push it on opStack
        # after moving all operators of equal or higher precedence
        # from opStack to output
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[c]):
                postfix.append(opStack.pop())
            opStack.push(c)
            
    # move remaining operators from opStack to output
    while not opStack.isEmpty():
        postfix.append(opStack.pop())
    
    return ' '.join(postfix)
# end f. infix2postfix            
    

def main():
    infix = input('Enter an infix expression: ')
    postfix = infix2postfix(infix)
    print('Infix: ', infix)
    print('Associated Postfix: ', postfix)
    

main()
    