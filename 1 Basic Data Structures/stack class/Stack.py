# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 08:33:45 2020

@author: virustous
"""


# stack implementation
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]