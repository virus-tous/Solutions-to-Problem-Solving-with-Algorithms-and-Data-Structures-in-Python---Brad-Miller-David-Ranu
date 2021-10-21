# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 20:29:26 2021

@author: virustous
"""

'''
Modify the postfix evluation algorithm so that it can handle errors.
'''

from Stack import Stack

def isValidPostfix(postfix):
    '''check if postfix expr contains invalid token'''
    postfix = postfix.strip()
    tokenList = postfix.split()
    ops = ['^', '*', '/', '+', '-']
    for c in tokenList:
        if (c not in ops) and (not c.isnumeric()):
            return False
    return True
# end f. validatePostfix


def doMath(n1, n2, op):
    if op == '^':
        return n1 ** n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 / n2
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
# end f. doMath


def eval_postfix(postfix):
    '''evaluate a postfix expression using stack'''
    if not isValidPostfix(postfix):
        raise Exception('Invalid Postfix Expression!')
        
    # ops = ['^', '*', '/', '+', '-']
    operandStack = Stack()
    
    tokenList = postfix.strip().split()
    for c in tokenList:
        if c.isnumeric():
            operandStack.push(int(c))
        else:
            try:
                # check if there are enuf operands to pop
                n2 = operandStack.pop()
                n1 = operandStack.pop()
            except:
                raise Exception("Invalid Postfix Expression!!")
            operandStack.push(doMath(int(n1), int(n2), c))
    return operandStack.pop()
# end f. eval_postfix

def main():
    postfix = input('Enter a postfix expression: ')
    print(postfix, ' = ', eval_postfix(postfix))
    
#main()
                
            