# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:17:16 2021

@author: virustous
"""

'''
5. Queue Implementation using the end of a list as its rear
front <== rear
enqueue O(1)
dequeue O(n-1)
'''

class Queue:
    def __init__(self):
        self._items = []
        
    def isEmpty(self):
        return self._items == []
    
    def size(self):
        return len(self._items)
    
    def enqueue(self, item):
        self._items.append(item)
        
    def dequeue(self):
        if self._items == []:
            raise Exception('Queue is empty!')
        return self._items.pop(0)