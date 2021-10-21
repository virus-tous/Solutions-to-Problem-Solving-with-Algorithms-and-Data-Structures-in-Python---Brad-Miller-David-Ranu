# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:02:50 2021

@author: virustous
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    
    def setData(self, newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext