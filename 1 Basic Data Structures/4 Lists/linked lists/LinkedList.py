# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:26:18 2021

@author: virustous
"""

import Node

# unordered list implementation: Linked List
class LinkedList:
    def __init__(self):
        '''LL constructor'''
        self.head = None
        
    def isEmpty(self):
        '''check if head points to none'''
        return self.head == None
    
    def add(self, item):
        '''add a new item right at the head (beginning)
        O(1)
        '''
        temp = Node.Node(item) # make a temp node for item
        temp.setNext(self.head) # temp refers to old head
        self.head = temp   # temp is new head
        
    # linked list traversal
    
    def size(self):
        '''return size of a ll
        O(n)
        '''
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.getNext()
        return count
    
    def search(self, item):
        '''search for the occurrence of item in the ll
        O(n)
        '''
        curr = self.head
        while curr != None:
            if curr.getData() == item:
                return True
            curr = curr.getNext()
        return False    # not found
    
    def remove(self, item):
        '''remove node of val item from the ll
        O(n)
        '''
        curr = self.head
        prev = None
        found = False
        # suppose item is on ll
        while not found:
            # pos of item found > end while
            if curr.getData() == item:
                found = True
            # item still not found, prev and curr move 
            # 1 node ahead
            else:
                prev = curr
                curr = curr.getNext()
                
        # if item to be removed is 1st item,
        # make head refer to the node after curr node
        if prev == None:
            self.head = curr.getNext()
        # otherwise, change prev reference to omit curr node
        else:
            prev.setNext(curr.getNext())