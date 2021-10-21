# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:29:02 2021

@author: virustous
"""

import Node

class OrderedList:
    def __init__(self):
        self.head = None    # empty list
        
    def size(self):
        '''return size of ordered list
        O(n)
        '''
        curr = self.head
        count = 0
        while curr != None:
            curr = curr.getNext()
            count += 1
        return count
    
    def isEmpty(self):
        '''check if ordered list is empty'''
        return self.head == None
    
    def search(self, item):
        '''check if item is on ordered list
        O(n)
        '''
        curr = self.head
        while curr != None:
            if curr.getData() == item:
                return True
            elif curr.getData() > item:
                return False
            curr = curr.getNext()
        # if all elements < item
        return False
    
    def add(self, item):
        '''add a new item to the proper position
        O(n)
        '''
        prev = None
        curr = self.head
        while (curr != None) and (curr.getData() < item):
            prev = curr
            curr = curr.getNext()
        
        # create a node for val item
        temp = Node.Node(item)
        # if item is smallest, add at the head
        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        # otherwise, add in some place in the middle
        else:
            temp.setNext(curr)
            prev.setNext(temp)