# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:50:44 2021

@author: virustous
"""

import Stack

s = Stack.Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())