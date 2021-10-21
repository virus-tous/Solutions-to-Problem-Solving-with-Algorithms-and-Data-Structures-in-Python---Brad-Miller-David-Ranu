# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 13:55:24 2021

@author: virustous
"""

# Queue implementation
class Queue:
    def __init__(self):
        self._items = []
        
    def isEmpty(self):
        return self._items == []
    
    def enqueue(self, e):
        self._items.insert(0, e)
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty!')
        return self._items.pop()
    
    def size(self):
        return len(self._items)
# end class Queue