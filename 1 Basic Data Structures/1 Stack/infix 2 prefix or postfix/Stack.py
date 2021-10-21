# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:25:27 2021

@author: virustous
"""

class Stack:
    def __init__(self):
        self._items = []
        
    def push(self, item):
        '''push an item on top of the stack'''
        self._items.append(item)
        
    def pop(self):
        '''remove the top item from the stack'''
        if self.isEmpty():
            raise Exception("stack is empty!!!")
        return self._items.pop()
        
    def peek(self):
        '''return the top item of the stack'''
        if self.isEmpty():
            raise Exception('stack is empty!!!')
        return self._items[-1]
    
    def isEmpty(self):
        '''check if the stack is empty'''
        return self._items == []
    
    def size(self):
        '''return the size of the stack'''
        return len(self._items)