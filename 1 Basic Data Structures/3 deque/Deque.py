# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:12:02 2021

@author: virustous
"""

# Deque implementation in Py
class Deque:
    def __init__(self):
        self._items = []
    
    def addRear(self, e):
        self._items.insert(0, e)
    
    def addFront(self, e):
        self._items.append(e)
        
    def removeRear(self):
        if self._items == 0:
            raise Exception('Deque is Empty!')
        return self._items.pop(0)
    
    def removeFront(self):
        if self._items == 0:
            raise Exception('Deque is Empty!')
        return self._items.pop()
    
    def isEmpty(self):
        return self._items == []
    
    def size(self):
        return len(self._items)