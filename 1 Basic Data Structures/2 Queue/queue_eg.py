# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:27:10 2021

@author: virustous
"""

import Queue

q = Queue.Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()

print(q.size())