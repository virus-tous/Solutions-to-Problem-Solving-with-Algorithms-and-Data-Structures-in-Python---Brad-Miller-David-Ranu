# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 21:58:45 2021

@author: virustous
"""

from _1_complete_infix2postfix import infix2postfix
from _2_complete_postfix_evaluation import eval_postfix

infix = input('Enter an infix expression: ')
postfix = infix2postfix(infix)

print(infix, ' = ', eval_postfix(postfix))