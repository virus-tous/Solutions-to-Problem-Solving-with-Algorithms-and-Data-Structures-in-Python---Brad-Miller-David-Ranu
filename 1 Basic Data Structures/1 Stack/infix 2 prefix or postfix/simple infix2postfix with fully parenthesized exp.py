# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:20:44 2021

@author: virustous
"""

def simpleInfix2Postfix(expr):
    '''infix2postfix with a fully parenthesized expression
    move the operator to the position of its right parenthesis'''
    operators = []
    output = []
    for token in expr:
        # token is left para -> push it on operators
        if token == '(':
            operators.append(token)
        # pop its operator from operators and push it on output
        elif token == ')':
            # pop the corresponding operator
            output.append(operators.pop())
            # pop the corresponding para
            operators.pop()
        elif token in ('+', '-', '*', '/'):
            operators.append(token)
        # token is an operand -> push it on output
        else:
            output.append(token)
    return ''.join(output)

print(simpleInfix2Postfix('((A*B)+(C*D))'))
print(simpleInfix2Postfix('(A+(B*C))'))
print(simpleInfix2Postfix('((A+B)*C)'))
print(simpleInfix2Postfix('(((A+B)*C)-((D-E)*(F+G)))'))
    